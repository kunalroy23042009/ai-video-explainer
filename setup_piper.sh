#!/usr/bin/env bash
# Downloads and installs Piper TTS for narration

set -e
PIPER_VERSION="1.2.0"
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

echo "📦 Downloading Piper TTS v${PIPER_VERSION}..."

ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
  URL="https://github.com/rhasspy/piper/releases/download/v${PIPER_VERSION}/piper_amd64.tar.gz"
elif [ "$ARCH" = "aarch64" ]; then
  URL="https://github.com/rhasspy/piper/releases/download/v${PIPER_VERSION}/piper_arm64.tar.gz"
else
  echo "❌ Unsupported architecture: $ARCH"; exit 1
fi

curl -L "$URL" | tar -xz -C "$INSTALL_DIR"
echo "✅ Piper installed to $INSTALL_DIR/piper"

echo "📥 Downloading default voice: en_US-lessac-medium..."
VOICE_DIR="$HOME/.local/share/piper/voices"
mkdir -p "$VOICE_DIR"
curl -L "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx" \
     -o "$VOICE_DIR/en_US-lessac-medium.onnx"
curl -L "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json" \
     -o "$VOICE_DIR/en_US-lessac-medium.onnx.json"

echo "✅ Setup complete! Run: python main.py --prompt \"Your topic here\""
