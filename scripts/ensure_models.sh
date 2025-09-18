#!/usr/bin/env bash
set -euo pipefail
CHAT_MODEL="${OLLAMA_CHAT_MODEL:-llama3.1:8b}"
EMBED_MODEL="${OLLAMA_EMBED_MODEL:-nomic-embed-text}"

have_model () {
  ollama list | awk '{print $1}' | grep -qx "$1"
}

echo "Checking Ollama models..."
if ! have_model "$CHAT_MODEL"; then
  echo "Pulling chat model: $CHAT_MODEL"
  ollama pull "$CHAT_MODEL"
fi
if ! have_model "$EMBED_MODEL"; then
  echo "Pulling embed model: $EMBED_MODEL"
  ollama pull "$EMBED_MODEL"
fi
echo "Models ready."
