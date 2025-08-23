cat > docker-entrypoint.sh << 'EOF'
#!/bin/sh
set -e
# If Firebase JSON is provided as a secret, write it to a file
if [ -n "$FIREBASE_CREDENTIALS_JSON" ]; then
  mkdir -p /secrets
  echo "$FIREBASE_CREDENTIALS_JSON" > /secrets/service-account.json
  chmod 600 /secrets/service-account.json
  export GOOGLE_APPLICATION_CREDENTIALS=/secrets/service-account.json
fi
exec "$@"
EOF