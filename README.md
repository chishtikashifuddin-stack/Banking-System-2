# Versatile Bank System

<p align="center">
  A simple and versatile command-line banking system developed using Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Storage-JSON-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

# Overview

Versatile Bank System is a Python-based command-line banking application that simulates real-world banking operations such as:

- Account Creation
- Balance Management
- Credit/Debit Operations
- Fund Transfers
- Transaction History Tracking

The project is designed for learning Python fundamentals, file handling, and JSON-based data management.

---

# Features

## Admin Panel

- Create User Accounts
- View Account Details
- Transfer Funds Between Users
- Manage Banking Records

---

## User Panel

- Credit Money
- Debit Money
- Transfer Funds
- Check Account Balance
- View Transaction History

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| JSON | Data Storage |
| File Handling | Record Management |
| pywhatkit | WhatsApp Notifications |
| datetime | Date & Time |
| random | Random Account Generation |
| os | System Operations |

---

# Project Structure

```text
Versatile-Bank/
│
├── main.py
├── requirements.txt
├── admin_bank_DB.txt
├── user_bank_DB.txt
├── user_history.txt
├── transfer_history.txt
├── screenshots/
│   ├── home.png
│   ├── admin-panel.png
│   ├── transaction.png
│   └── history.png
│
├── demo/
│   └── versatile-bank-demo.gif
│
└── README.md
```

---

# Installation

## Automatic Installation

### Windows

Run:

```bash id="5u9f1m"
setup.bat
```

### Linux / macOS

Run:

```bash id="5l7pja"
bash setup.sh
```

---

# Manual Installation

## Step 1: Clone Repository

```bash id="nq39pm"
git clone https://github.com/your-username/Versatile-Bank.git
```

---

## Step 2: Open Project Folder

```bash id="pn2y6t"
cd Versatile-Bank
```

---

## Step 3: Install Dependencies

```bash id="v1z03m"
pip install -r requirements.txt
```

---

## Step 4: Run Application

```bash id="g5y52z"
python main.py
```

---

# requirements.txt

```txt
pywhatkit
```

---

# Installation Automation

## setup.sh

```bash
#!/bin/bash

echo "Installing Required Packages..."
pip install -r requirements.txt

echo "Starting Versatile Bank..."
python main.py
```

---

## setup.bat

```bat
@echo off

echo Installing Required Packages...
pip install -r requirements.txt

echo Starting Versatile Bank...
python main.py

pause
```

---

# Sample Application Flow

```text
1. Start Application
2. Select User Type
   ├── Admin
   └── User

3. Perform Banking Operations
   ├── Create Account
   ├── Credit Money
   ├── Debit Money
   ├── Transfer Funds
   └── View History
```

---

# Data Storage Files

| File Name | Description |
|-----------|-------------|
| admin_bank_DB.txt | Stores Admin Records |
| user_bank_DB.txt | Stores User Accounts |
| user_history.txt | Stores Transaction History |
| transfer_history.txt | Stores Transfer Records |

---

# Limitations

- No Authentication System
- Plain Text Data Storage
- Local Machine Only
- No Database Integration
- Not Production Ready

---

# Future Improvements

- Secure Login System
- SQLite/MySQL Integration
- GUI with Tkinter
- Flask/Django Web Version
- OTP Verification
- Enhanced Security
- Account Statement Generation
- Cloud Database Support

---

# Learning Outcomes

This project helps in understanding:

- Python Fundamentals
- File Handling
- JSON Manipulation
- Transaction Logic
- Program Flow Management

---

# Security Notice

This project is developed for educational purposes only.

Do not use it for real banking or financial systems.

---

# Contributing

Contributions are welcome.

Steps to contribute:

1. Fork Repository
2. Create New Branch
3. Commit Changes
4. Open Pull Request

---

# Author

## Kashifuddin Chishti

Python Developer.

---

# License

This project is for educational purposes only.

---

# Support

If you liked this project:

- Star the Repository
- Fork the Project
- Share with Others

---

<p align="center">
  Made with ❤️ using Python
</p>
