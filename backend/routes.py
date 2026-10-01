import os

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ai_core.gemini_generator import (
    GeminiConfigurationError,
    GeminiDocumentGenerator,
)


router = APIRouter()

_generator = None


class DocumentRequest(BaseModel):
    document_type: str = Field(..., min_length=2)
    parties: str = Field(..., min_length=2)
    terms: list[str] = Field(..., min_length=1)
    effective_date: str
    additional_instructions: str = ""


def get_generator():
    global _generator

    if _generator is None:
        _generator = GeminiDocumentGenerator()

    return _generator


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "gemini_configured": bool(
            os.getenv("GEMINI_API_KEY", "").strip()
        ),
    }


@router.post("/generate")
def generate_document(request: DocumentRequest):

    try:
        generator = get_generator()

        content = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date,
            additional_instructions=request.additional_instructions,
        )

        return {
            "document_type": request.document_type,
            "content": content,
        }

    except GeminiConfigurationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        )

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        )