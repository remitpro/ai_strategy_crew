from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from .crew import crew
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
