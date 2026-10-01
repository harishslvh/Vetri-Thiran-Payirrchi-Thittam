# ⚖️ LegalEase - AI-Powered Legal Document Generator

LegalEase is an AI-powered legal document drafting application that helps users generate customizable legal document drafts from simple user-provided information.

The application provides an editable document preview and allows users to export the generated draft as TXT, DOCX, or PDF.

> ⚠️ **Disclaimer:** LegalEase generates AI-assisted legal document drafts. These drafts should be reviewed by a qualified legal professional before use. LegalEase does not provide legal advice.

---

## 🚀 Features

- 🤖 AI-assisted legal document generation using Google Gemini
- 📄 Supports multiple document types
- ✏️ Editable document preview
- 📥 Download documents as TXT
- 📝 Download documents as DOCX
- 📕 Download documents as PDF
- 🎯 Demo Mode for testing without Gemini API generation
- ⚠️ API error and quota handling
- 📅 Effective date input
- 👥 Party information input
- 📋 Key terms and additional instructions

---

## 📑 Supported Document Types

LegalEase currently provides options for:

- Employment Agreement
- Lease Agreement
- Non-Disclosure Agreement
- Service Agreement
- Other

---

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

### Document Processing
- python-docx
- FPDF

### Other Technologies
- Python
- Requests
- python-dotenv
- Pillow

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  │ HTTP Request
  ▼
FastAPI Backend
  │
  ▼
Gemini AI
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