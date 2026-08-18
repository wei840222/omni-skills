#!/usr/bin/env bash
# Initialize writing workspace
set -euo pipefail

WORKSPACE="${1:?Usage: init-workspace.sh <path>}"

mkdir -p "$WORKSPACE"/{pieces,versions,audits,research}

if [[ ! -e "$WORKSPACE/config.json" ]]; then
cat > "$WORKSPACE/config.json" << 'EOF'
{
  "depth": "standard",
  "auto_audit": true,
  "created": "'"$(date -Iseconds)"'"
}
EOF
fi

if [[ ! -e "$WORKSPACE/index.json" ]]; then
cat > "$WORKSPACE/index.json" << 'EOF'
{
  "pieces": []
}
EOF
fi

echo "✅ Workspace initialized at $WORKSPACE"
echo "   - pieces/    : active writing pieces"
echo "   - versions/  : automatic backups"
echo "   - audits/    : quality reports"
echo "   - research/  : research notes"
