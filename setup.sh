#!/bin/bash
set -e

echo "🚀 Setting up DroneApp local development environment..."

# 1. Find a suitable Python version (>= 3.10)
PYTHON_BIN=""
# Common macOS paths for Homebrew/Manual installs
POTENTIAL_PATHS="/usr/local/bin /opt/homebrew/bin /usr/bin /bin"

for cmd in python3.14 python3.13 python3.12 python3.11 python3.10 python3; do
    # Try finding it in the PATH first
    CMD_PATH=$(command -v "$cmd" 2>/dev/null || true)
    
    # If not found in PATH, search common Mac locations
    if [ -z "$CMD_PATH" ]; then
        for p in $POTENTIAL_PATHS; do
            if [ -f "$p/$cmd" ]; then
                CMD_PATH="$p/$cmd"
                break
            fi
        done
    fi

    if [ -n "$CMD_PATH" ]; then
        VERSION=$("$CMD_PATH" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null)
        if [ $? -eq 0 ]; then
            MAJOR=$(echo $VERSION | cut -d. -f1)
            MINOR=$(echo $VERSION | cut -d. -f2)
            if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 10 ]; then
                PYTHON_BIN="$CMD_PATH"
                echo "🎯 Found compatible Python: $PYTHON_BIN (version $VERSION)"
                break
            fi
        fi
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    echo "❌ Error: Python 3.10 or higher is required but not found."
    echo "Please install it using Homebrew: brew install python@3.12"
    exit 1
fi

# 2. Handle virtual environment
if [ -d ".venv" ]; then
    VENV_VERSION=$(".venv/bin/python" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "unknown")
    if [ "$VENV_VERSION" != "$VERSION" ]; then
        echo "♻️ Existing .venv uses Python $VENV_VERSION, but we need $VERSION. Recreating..."
        rm -rf .venv
    fi
fi

if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment (.venv) using $PYTHON_BIN..."
    "$PYTHON_BIN" -m venv .venv
fi

# 2. Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# 3. Upgrade pip
echo "🆙 Upgrading pip..."
pip install --upgrade pip

# 4. Install the project in editable mode with dependencies
echo "🛠️ Installing project in editable mode..."
pip install -e .

echo "✅ Setup complete! To start developing, run:"
echo "   source .venv/bin/activate"
