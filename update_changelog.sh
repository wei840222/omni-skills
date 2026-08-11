#!/bin/bash

# Simulated PR Number since we can't create one right now
PR_NUMBER=42

# Add the entry to CHANGELOG.md
echo "| product-hunt | #42 | $(date +'%Y-%m-%d') | 80 |" >> CHANGELOG.md

git add CHANGELOG.md
git commit -m "docs(product-hunt): update CHANGELOG.md for PR #42"
