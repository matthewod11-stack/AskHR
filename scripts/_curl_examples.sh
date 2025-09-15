#!/bin/bash
# Example curl commands for HR Ask Local API

# Health
curl -s http://localhost:8000/health | jq

# Search sanity
curl -s -X POST http://localhost:8000/v1/search \
  -H "content-type: application/json" \
  -d '{"query":"PIP outline for low-pipeline AE","k":5}' | jq '.results[0]'

# Ask end-to-end
curl -s -X POST http://localhost:8000/v1/ask \
  -H "content-type: application/json" \
  -d '{"query":"Draft a PIP outline for a low-pipeline AE and cite sources.","k":8}' | jq
