# 🔐 TASK 3: Secure Coding Review

## 📌 Overview
This project focuses on performing a **Secure Coding Review** on a Python Flask-based application.  
The goal is to identify security vulnerabilities and apply best practices to improve application security.

---

## 📋 Task Requirements

| Requirement | Status |
|------------|--------|
| Select a programming language & application | ✅ |
| Perform code review for vulnerabilities | ✅ |
| Use static analysis / manual inspection | ✅ |
| Provide recommendations & best practices | ✅ |
| Document findings & remediation steps | ✅ |

---


## 🎯 Objective

- Select an application to audit  
- Perform code review to identify vulnerabilities  
- Use static analysis and manual inspection  
- Provide recommendations for secure coding  
- Document findings and remediation steps  

---
## 🧪 Application Details

- Language: Python 🐍  
- Framework: Flask 🌐  
- Database: SQLite 🗄️  

The app includes:
- User login system  
- Database storage  
- Password hashing (bcrypt)  
---
## 🔍 Security Findings

### ❌ 1. Hardcoded Secret Key
```python
app.secret_key = "supersecretkey"
```
###🔴 Risk: Session hijacking
###✅ Fix: Use environment variables
---
## 📁 Project Structure
```bash
TASK 3 Secure Coding Review/
├── templates/        → HTML templates (UI pages)
├── venv/             → Virtual environment (can be ignored in repo)
├── add_user.py       → Script to add users to database
├── app.py            → Main application file
├── database_db.py    → Database connection & setup
└── users.db          → SQLite database file
└── README.md         → Documentation
```


## ▶️ How to Run
1. Open "CMD" or Power Shell
2. Navigate to the project directory e.g.:

```bash
cd "F:\Internships DATA\CodeAlpha\Cyber Security Tasks\TASK 3 Secure Coding Review"
```
3. Set execution policy (Windows PowerShell only)
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
4. Activate virtual environment:
```bash
.\venv\Scripts\Activate
```
5. Run the application:
```bash
python app.py

⚠️ Note: "warnings.warn(
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit"
leave it in running mode and go to the web Browser 
```
6. Open in browser:
```bash
Type "http://127.0.0.1:5000"
```
