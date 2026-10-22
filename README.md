# Document RAG Assistant

A document question-answering system built with Retrieval-Augmented Generation (RAG).

The project aims to support document upload, text extraction, chunking, semantic retrieval, and LLM-based question answering with source citations.

## Current Progress

- [x] React frontend setup
- [x] FastAPI backend setup
- [x] PDF upload API
- [x] PDF text extraction with PyMuPDF
- [x] Basic text chunking
- [x] Unit tests for PDF parsing and chunking
- [ ] Document chunking with metadata
- [ ] Embedding generation
- [ ] Vector search
- [ ] RAG question answering
- [ ] Source citation
- [ ] Frontend document upload and chat interface
- [ ] Docker support
- [ ] RAG evaluation

## Tech Stack

### Frontend
- React
- Vite

### Backend
- Python
- FastAPI

### Document Processing
- PyMuPDF

### Testing
- pytest

## Project Structure

```text
document-rag-assistant/
├── app/
│   └── document/
│       ├── parser.py
│       └── chunker.py
├── frontend/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```
## for yuwen

### Linux 指令

把資料夾在vscode開啟
```
code .
```
開啟資料夾路徑
```
explorer.exe .
\\wsl$\Ubuntu\home\tiffany\ai-agent-sandbox
```
確認docker連線
```
docker ps
```

### 啟動 FastAPI 後端(ubuntu 1)
```
cd ~/ai-agent-sandbox
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
### 啟動 Vue 前端(ubuntu 2)
```
cd ~/ai-agent-sandbox/frontend
npm run dev
```
