# mini-rag

A small FastAPI app intended as a project for learning and experimenting with a
mini-RAG.

## Installation (macOS)

macOS installation using Homebrew and `uv`. Then sync dependencies directly from
`pyproject.toml`.

```bash
brew install uv

# Work from the src folder where pyproject.toml lives
cd src

# Create the environment and install runtime deps from pyproject
uv sync

# Install dev tools and enable git hooks (perk)
uv pip install prek ty
prek install
```

### Windows/Linux

For non-macOS platforms, follow the official guides:

- uv installation: <https://docs.astral.sh/uv/getting-started/installation/>
- Python (Windows): <https://www.python.org/downloads/windows/>
- Python (Linux): <https://www.python.org/downloads/source/> (or install via
  your distro's package manager)

## Configuration

Create a `.env` file in the repo root to customize the welcome route:

```env
APP_NAME=mini-rag
APP_VERSION=0.1.0
```

## Run

The FastAPI app is defined as `app` in [src/main.py](src/main.py). Run from the
`src` directory using `uv`:

```bash
cd src
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open <http://localhost:8000/docs> for interactive API docs.

### Quick Check

The base route is implemented in [src/routes/base.py](src/routes/base.py) and
returns a message built from your `.env`:

```bash
curl http://localhost:8000/api/v1/
# {"message":"Welcome to the mini-rag API! 0.1.0"}
```

## Development

Minimal, learning-focused setup:

- **Runtime:** FastAPI + Uvicorn
- **Env:** `.env` via `python-dotenv`
- **Uploads:** `python-multipart`
- **Hooks:** `prek` installed and enabled (`prek install`)

## Thanks

Special thanks to **@bakrianoo** for guidance.
