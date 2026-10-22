from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI(
    title="Document RAG Assistant",
    description="A RAG-based assistant for document question answering.",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "Document RAG Assistant API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    content = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content)
    }