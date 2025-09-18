
#!/usr/bin/env bash
set -euo pipefail
URL="${1:-http://localhost:8000/health}"
ALT="${2:-http://127.0.0.1:8000/health}"
echo "[wait_for_api] waiting for ${URL} (fallback ${ALT})"
for i in {1..60}; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -m 1 "$URL" || echo "")
  if [[ "$code" == "200" ]]; then
    echo "[wait_for_api] API is up at ${URL}"
    exit 0
  fi
  code2=$(curl -s -o /dev/null -w "%{http_code}" -m 1 "$ALT" || echo "")
  if [[ "$code2" == "200" ]]; then
    echo "[wait_for_api] API is up at ${ALT}"
    exit 0
  fi
  sleep 1
done
echo "[wait_for_api] API did not become ready. Last logs:"
tail -n 60 logs/api.log || true
exit 1
