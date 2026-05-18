# 🏦 Versatile Bank System (Python Project)

## 📌 Overview

Versatile Bank is a **command-line banking system** built using Python.
It simulates real-world banking operations such as account creation, balance management, transactions, and history tracking.

This project is designed to demonstrate **file handling, JSON usage, and core Python programming concepts**.

---

## 🚀 Features

### 👨‍💼 Admin Panel

* Create new user accounts
* Check account details
* Transfer money between users

### 👤 User Panel

* Credit money
* Debit money
* Check account details
* View transaction history
* Transfer money to another user

---

## 🛠️ Technologies Used

* Python 🐍
* JSON (for data storage)
* File Handling
* `pywhatkit` (for WhatsApp notifications)
* `datetime`, `random`, `os`

---

## 📂 Project Structure

```
📁 Versatile-Bank
│
├── main.py
├── admin_bank_DB.txt
├── user_bank_DB.txt
├── user_history.txt
├── transfer_history.txt
└── README.md
```

---

## ⚙️ How to Run

1. Install Python (3.x)
2. Install required library:

   ```bash
   pip install pywhatkit
   ```
3. Run the program:

   ```bash
   python main.py
   ```

---

## 📸 Sample Flow

1. Start program
2. Choose:

   * `1` → Admin
   * `2` → User
3. Perform operations like:

   * Create account
   * Credit/Debit money
   * Transfer funds

---

## ⚠️ Limitations

* Data is stored in **text files (not secure)**
* No authentication system
* Duplicate records may occur
* Works only on local system
* Uses `os.popen` (not recommended for production)

---

## 🔐 Future Improvements

* ✅ Add login system (PIN/password)
* ✅ Use database (SQLite/MySQL)
* ✅ Build GUI (Tkinter)
* ✅ Convert to Web App (Flask/Django)
* ✅ Improve security & validation

---

## 💡 Learning Outcomes

* File handling in Python
* Working with JSON data
* Building CLI-based applications
* Managing program flow using functions

---

## 👨‍💻 Author

**Kashifuddin Chishti**

---

## ⭐ Support

If you like this project:

* Star ⭐ the repository
* Share with others

---

## 📜 License

This project is for educational purposes only.
