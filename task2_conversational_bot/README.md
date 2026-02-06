# Task 2 – Conversational Resume Bot

## Description

This project is an interactive conversational chatbot that answers questions based on a resume PDF.
The resume is converted into embeddings and stored in a FAISS vector database, allowing the user to ask
natural language questions such as skills, experience, and summary.

The chatbot runs in the terminal and maintains conversation history.

---

## Folder Structure

task2_conversational_bot/
- main.py
- requirements.txt
- README.md
- .env
- .gitignore
- Mahesh Updated Resume.pdf
- venv/

---

## Setup Instructions (Windows)

### 1. Open terminal inside task2_conversational_bot

```powershell
cd task2_conversational_bot
2. Create virtual environment
```powershell
python -m venv venv
Activate:
```powershell
.\venv\Scripts\Activate.ps1
If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Add resume PDF

Place your resume PDF in the same folder as main.py.

Update this line in main.py if needed:PDF_FILENAME = "Mahesh Updated Resume.pdf"
5. Run the chatbot
python main.py
