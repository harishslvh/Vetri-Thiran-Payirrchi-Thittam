import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


class GeminiConfigurationError(RuntimeError):
    pass


class GeminiDocumentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        ).strip()

        if not self.api_key:
            raise GeminiConfigurationError(
                "GEMINI_API_KEY is missing from the .env file."
            )

        self.client = genai.Client(api_key=self.api_key)

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        effective_date,
        additional_instructions="",
    ):
        terms_text = "\n".join(f"- {term}" for term in terms)

        prompt = f"""
You are an AI assistant helping draft a legal document.

Document type:
{document_type}

Parties:
{parties}

Effective date:
{effective_date}

Key terms:
{terms_text}

Additional instructions:
{additional_instructions}

Create a clear, professionally structured draft.

Important rules:
- Do not invent names, dates, amounts, addresses, obligations,
  governing law, or other facts that were not provided.
- If important information is missing, use a clear placeholder
  such as [INSERT INFORMATION].
- Use appropriate headings and numbered clauses.
- Keep the document editable and easy to read.
- This is a draft for review and is not a substitute for advice
  from a qualified legal professional.
"""
        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                )
                break

            except Exception as exc:
                error_text = str(exc)

                # Do not retry quota errors
                if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                    raise exc

                if attempt == 2:
                    raise exc

                time.sleep(5)

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text