# Loc Chat AI

Chat with your PDFs privately. Everything runs on your machine: the LLM and embeddings come from [Ollama](https://ollama.com), and your documents never leave your computer. There is no login and no cloud API.

## Features

- Upload a PDF and ask questions about it (RAG)
- Streaming answers with markdown rendering
- One document per chat, with saved chat history
- Light and dark mode

## Tech stack

- **Frontend:** Next.js (App Router), TypeScript, Tailwind CSS, shadcn/ui
- **Backend:** FastAPI, SQLAlchemy (SQLite), LangChain
- **Vector store:** Chroma (local files)
- **Models:** Ollama (chat model + `nomic-embed-text` embeddings)

## Requirements

- Python 3.12 and [uv](https://docs.astral.sh/uv/)
- Node.js 20+ and npm
- [Ollama](https://ollama.com/download)
- About 8 GB of RAM or VRAM for an 8B model (use a 3B model on weaker machines)

## Setup

### 1. Ollama

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

Make sure Ollama is running (`ollama serve`, or the desktop service).

### 2. Backend

From the project root:

```bash
uv sync
cp .env.example .env
uv run python backend/init_db.py
uv run python backend/main.py
```

The API runs on `http://127.0.0.1:8000`.

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://127.0.0.1:3000`.

## Configuration

Backend settings go in `.env` in the project root:

```env
OLLAMA_BASE_URL=http://127.0.0.1:11434
LLM_MODEL=llama3.1:8b
EMBEDDING_MODEL=nomic-embed-text
```

The frontend proxies `/api/v1/*` to the backend. To change the backend address, set `FASTAPI_URL` in `frontend/.env` (default `http://127.0.0.1:8000`).

## Project structure

```
backend/
  app/            FastAPI app (routers, services, models, RAG)
  storage/        SQLite DB, uploaded PDFs, Chroma data (not committed)
  main.py         Dev server entry point
  init_db.py      Creates the database tables
frontend/
  app/            Pages and layouts
  components/     UI and chat components
  lib/            API client and services
```

## Privacy notes

- Both servers should listen on `127.0.0.1` only. There is no authentication, so anyone who can reach the ports can read your documents.
- Don't expose ports 3000 or 8000 on your network.
- To confirm nothing leaves your machine, turn off Wi-Fi and use the app. It should still work.
- `backend/storage/` and `.env` are in `.gitignore`. Don't commit them.

## Changing models

- **Chat model:** change `LLM_MODEL`, then restart the backend.
- **Embedding model:** change `EMBEDDING_MODEL`, then delete `backend/storage/chroma` and re-upload your documents. Vectors from different embedding models are not compatible.

## Troubleshooting

- **Connection refused to Ollama:** check that Ollama is running and `OLLAMA_BASE_URL` is correct.
- **Model not found:** run `ollama pull <model>` for the model named in `.env`.
- **Answers cut off or ignore the document:** small models struggle with long context. Try a larger model, or raise the context size (`num_ctx`) in the LLM setup.
- **Upload fails during ingestion:** Ollama must be running, since embeddings are created at upload time.
- **Stale or empty answers after changing the embedding model:** delete `backend/storage/chroma` and re-upload.

## Reset all data

```bash
rm -rf backend/storage
uv run python backend/init_db.py
```