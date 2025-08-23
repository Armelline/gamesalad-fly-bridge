#!/bin/sh
set -e
if [ -n "$FIREBASE_CREDENTIALS_JSON_B64" ]; then
  mkdir -p /secrets
  printf '%s' "$FIREBASE_CREDENTIALS_JSON_B64" | base64 -d > /secrets/service-account.json
  chmod 600 /secrets/service-account.json
  export GOOGLE_APPLICATION_CREDENTIALS=/secrets/service-account.json
elif [ -n "$FIREBASE_CREDENTIALS_JSON" ]; then
  # fallback (kept for compatibility)
  mkdir -p /secrets
  printf '%s' "$FIREBASE_CREDENTIALS_JSON" > /secrets/service-account.json
  chmod 600 /secrets/service-account.json
  export GOOGLE_APPLICATION_CREDENTIALS=/secrets/service-account.json
fi
exec "$@"
