# Task 1 – Multi-Agent Company Research

## Description
1.This project uses LangChain and OpenAI to research any company name provided by the user.
It automatically searches the web and returns:

- Company overview  
- Products / services  
- Recent news  
- Market position  

The output is displayed directly in the terminal.

---

## Folder Structure

task1_multi_agent/
- main.py
- requirements.txt
- README.md
- .env
- venv/

---

## Setup Instructions (Windows)

### 1. Open terminal inside task1_multi_agent

```powershell
cd task1_multi_agent
2.Create virtual environment
```powershell
python -m venv venv
Activate:
```powershell
.\venv\Scripts\Activate.ps1
if blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
3. Install dependencies
```powershell
pip install -r requirements.txt
4. Run the project
```powershell
python main.py
Enter any company name when prompted.


