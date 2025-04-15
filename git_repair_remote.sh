#!/bin/bash

echo "📁 Moving to project directory..."
cd ~/Desktop/Full-Spec_Thread_Extract || { echo '❌ Folder not found!'; exit 1; }

echo "🔍 Checking for .git directory..."
if [ ! -d .git ]; then
    echo "🔧 Initializing new Git repository..."
    git init
else
    echo "✅ Git already initialized."
fi

echo "🔁 Resetting remote origin (if exists)..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/MeatheadsMarketing/ThreadFullSpectrumExtraction.git

echo "✅ Remote set to: https://github.com/MeatheadsMarketing/ThreadFullSpectrumExtraction.git"

echo "📦 Staging and committing changes..."
git add .
git commit -m '🎛️ v1.0-ui-patch: Enhanced Streamlit dashboard'

echo "🏷️ Tagging version as v1.0-ui-patch..."
git tag v1.0-ui-patch

echo "🚀 Pushing to GitHub..."
git push origin main --tags --force

echo "✅ Push complete. Your repo is now live with v1.0-ui-patch!"