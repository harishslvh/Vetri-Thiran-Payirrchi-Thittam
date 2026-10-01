# ⚖️ LegalEase - AI-Powered Legal Document Generator

LegalEase is an AI-powered application designed to help users create customizable legal document drafts using simple inputs.

The application uses Google Gemini for AI-assisted document generation and provides an editable preview. Users can download the document in TXT, DOCX, or PDF format.

> ⚠️ **Legal Disclaimer:** LegalEase generates AI-assisted legal document drafts for informational and drafting purposes. The generated documents should be reviewed by a qualified legal professional before use. LegalEase does not provide legal advice.

## 🚀 Features

- 🤖 AI-assisted legal document generation
- 📄 Multiple document types
- ✏️ Editable document preview
- 📥 TXT download
- 📝 DOCX download
- 📕 PDF download
- 🎯 Demo Mode for testing without Gemini API requests
- ⚠️ API error and quota handling
- 📅 Effective date input
- 👥 Party information input
- 📋 Key terms and additional instructions

## 📑 Document Types

LegalEase currently supports:

- Employment Agreement
- Lease Agreement
- Non-Disclosure Agreement
- Service Agreement
- Other

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- FastAPI
- Pydantic
- Uvicorn

### AI
- Google Gemini API
- Google GenAI Python SDK

### Document Generation
- Python
- python-docx
- FPDF

### Other Libraries
- Requests
- python-dotenv
- Pillow

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
Google Gemini API
  │
  ▼
Generated Legal Draft
  │
  ▼
Editable Preview
  │
  ├── TXT
  ├── DOCX
  └── PDF
