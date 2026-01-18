from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

from .crew import crew
from .report_generator import create_strategy_document
import pdfplumber
import io

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StrategyRequest(BaseModel):
    strategy_content: str

@app.post("/export-strategy")
async def export_strategy(request: StrategyRequest):
    try:
        if not request.strategy_content:
             raise HTTPException(status_code=400, detail="No content to export.")

        doc_stream = create_strategy_document(request.strategy_content)
        
        return StreamingResponse(
            doc_stream, 
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": "attachment; filename=ai_strategy_roadmap.docx"}
        )

    except Exception as e:
        print(f"Error generating doc: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-strategy")
async def generate_strategy(file: UploadFile = File(...)):
    filename = file.filename.lower()
    content = ""
    
    try:
        if filename.endswith(".pdf"):
            # Use pdfplumber to extract text
            with pdfplumber.open(file.file) as pdf:
                for page in pdf.pages:
                    content += page.extract_text() or ""
        else:
            # Assume text/markdown
            file_bytes = await file.read()
            content = file_bytes.decode("utf-8")
            
        if not content.strip():
             raise HTTPException(status_code=400, detail="Could not extract text from file.")

        print(f"Extracted {len(content)} characters. Kickstarting crew...")
        
        # Run crew
        result = crew.kickoff(inputs={'digital_strategy': content})
        
        return {"result": str(result)}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
