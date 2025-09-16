#!/usr/bin/env bash
# One-click launcher for Ask HR (Ollama + FastAPI + Streamlit)
set -euo pipefail

# --- repo paths ---
# Fix: point to this script's directory (repo root), not its parent
ROOT="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$ROOT/logs"
mkdir -p "$LOG_DIR"

# --- config you can tweak ---
API_PORT="${API_PORT:-8000}"                 # change to 8010 if you prefer
UI_PORT="${UI_PORT:-8501}"
API_URL="http://localhost:${API_PORT}"
export API_URL                               # Streamlit reads this
export CHROMA_DISABLE_TELEMETRY=1
export TOKENIZERS_PARALLELISM=false

# New toggles for tab closing (macOS only)
CLOSE_HOST_TABS="${CLOSE_HOST_TABS:-true}"          # true|false
CLOSE_ALL_LOCALHOST="${CLOSE_ALL_LOCALHOST:-false}" # true|false
# Optionally pick a browser to open the UI: e.g., BROWSER="Google Chrome"
BROWSER="${BROWSER:-}"

echo "[launch] Using API_PORT=${API_PORT}, UI_PORT=${UI_PORT}"
echo "[launch] CLOSE_HOST_TABS=${CLOSE_HOST_TABS}, CLOSE_ALL_LOCALHOST=${CLOSE_ALL_LOCALHOST}"

cleanup() {
  echo "[launch] shutting down..."
  [[ -n "${UI_PID:-}" ]] && kill "${UI_PID}"  >/dev/null 2>&1 || true
  [[ -n "${API_PID:-}" ]] && kill "${API_PID}" >/dev/null 2>&1 || true
  [[ -n "${OLLAMA_PID:-}" ]] && kill "${OLLAMA_PID}" >/dev/null 2>&1 || true
}
trap cleanup INT TERM EXIT

# --- helpers ---

is_macos() { [[ "$(uname -s)" == "Darwin" ]]; }

wait_for_port() {
  # wait_for_port HOST PORT TIMEOUT_SECONDS
  local host="$1" port="$2" timeout="${3:-8}"
  local start now
  start="$(date +%s)"
  while true; do
    if nc -z "$host" "$port" >/dev/null 2>&1; then
      return 0
    fi
    now="$(date +%s)"
    if (( now - start >= timeout )); then
      return 1
    fi
    sleep 0.3
  done
}

close_tabs_in_browser() {
  # close_tabs_in_browser "Google Chrome" target1 target2 ...
  local app="$1"; shift
  local targets=("$@")

  # Only attempt if the app is running
  if ! pgrep -x "$app" >/dev/null 2>&1; then
    return 0
  fi

  # Pass targets as argv to AppleScript
  /usr/bin/osascript <<'APPLESCRIPT' "$app" "${targets[@]}"
on run argv
  set appName to item 1 of argv
  set targets to items 2 thru -1 of argv
  set closedCount to 0

  tell application appName
    set wins to every window
    repeat with w in wins
      try
        set tabsList to every tab of w
        set idxsToClose to {}
        set i to 1
        repeat with t in tabsList
          set theURL to ""
          try
            if appName is "Safari" then
              set theURL to URL of t
            else
              set theURL to (URL of t) as text
            end if
          end try
          repeat with needle in targets
            if (theURL contains (needle as text)) then
              set end of idxsToClose to i
              exit repeat
            end if
          end repeat
          set i to i + 1
        end repeat

        -- Close from highest index to lowest to avoid reindex problems
        set reversed to reverse of idxsToClose
        repeat with k in reversed
          try
            if appName is "Safari" then
              close tab (k as integer) of w
            else
              close tab (k as integer) of w
            end if
            set closedCount to closedCount + 1
          end try
        end repeat

        -- If the window is empty after closing, close the window
        try
          if (count of tabs of w) is 0 then close w
        end try

      end try
    end repeat
  end tell

  return closedCount
end run
APPLESCRIPT
}

close_localhost_tabs() {
  [[ "${CLOSE_HOST_TABS}" == "true" ]] || { echo "[launch] skipping tab close (CLOSE_HOST_TABS=false)"; return 0; }
  is_macos || { echo "[launch] skipping tab close (non-macOS)"; return 0; }

  local targets=()
  if [[ "${CLOSE_ALL_LOCALHOST}" == "true" ]]; then
    targets=("://localhost" "://127.0.0.1")
  else
    targets=("://localhost:${UI_PORT}" "://127.0.0.1:${UI_PORT}")
  fi

  # Close in each supported browser if running
  for app in "Google Chrome" "Brave Browser" "Microsoft Edge" "Safari"; do
    local count
    count="$(close_tabs_in_browser "$app" "${targets[@]}" 2>/dev/null || true)"
    if [[ -n "${count}" ]]; then
      echo "[launch] ${app}: closed ${count} tab(s) matching ${targets[*]}"
      # small settle delay helps some Chromium builds update window state
      sleep 0.2
    fi
  done
}

open_ui_tab() {
  local url="http://localhost:${UI_PORT}"
  if [[ -n "$BROWSER" ]]; then
    open -a "$BROWSER" "$url" >/dev/null 2>&1 || open "$url" >/dev/null 2>&1 || true
  else
    open "$url" >/dev/null 2>&1 || true
  fi
}

# --- activate venv if present ---
if [[ -f "$ROOT/.venv/bin/activate" ]]; then
  # shellcheck disable=SC1091
  source "$ROOT/.venv/bin/activate"
fi

# --- free ports if busy ---
for p in "${API_PORT}" "${UI_PORT}"; do
  if lsof -i :"$p" >/dev/null 2>&1; then
    echo "[launch] Port $p is busy. Attempting to free it..."
    # shellcheck disable=SC2009
    lsof -i :"$p" | awk 'NR>1 {print $2}' | xargs -r kill -9 || true
    sleep 1
  fi
done

# --- start Ollama if not running ---
if ! pgrep -x ollama >/dev/null 2>&1; then
  echo "[launch] starting Ollama..."
  ollama serve >"$LOG_DIR/ollama.log" 2>&1 &
  OLLAMA_PID=$!
  sleep 2
fi

# --- ensure models exist (optional, non-blocking) ---
(
  echo "[launch] ensuring models exist..." >>"$LOG_DIR/ollama.log"
  ollama list | grep -q "nomic-embed-text" || ollama pull nomic-embed-text >>"$LOG_DIR/ollama.log" 2>&1 || true
  ollama list | grep -q "llama3.1:8b"      || ollama pull llama3.1:8b      >>"$LOG_DIR/ollama.log" 2>&1 || true
) &

# --- start API ---
echo "[launch] starting API on ${API_URL} ..."
uvicorn app.main:app --host 0.0.0.0 --port "${API_PORT}" --reload >"$LOG_DIR/api.log" 2>&1 &
API_PID=$!

# --- start UI ---
echo "[launch] starting UI on http://localhost:${UI_PORT} ..."
# NOTE: update this path to your actual streamlit entry if different
streamlit run "$ROOT/ui/app.py" --server.port "${UI_PORT}" >"$LOG_DIR/ui.log" 2>&1 &
UI_PID=$!

# --- close old tabs, then open a fresh one ---
sleep 0.5
close_localhost_tabs
if wait_for_port "127.0.0.1" "${UI_PORT}" 10; then
  open_ui_tab
else
  echo "[launch] warning: UI not responding on port ${UI_PORT} yet; opening tab anyway."
  open_ui_tab
fi

echo "[launch] logs → $LOG_DIR"
echo "[launch] Ctrl+C in this window to stop everything."

# Wait for children; cleanup trap will fire on exit
wait
