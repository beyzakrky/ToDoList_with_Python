# ✅ To-Do List Application (Python)

## 📌 Project Overview

This project is a **command-line based task management application** developed in Python.
It allows users to efficiently organize and track their daily tasks with persistent data storage.

The application is designed with a focus on **modularity, error handling, and usability**, making it a solid learning project for software development fundamentals.

---

## 🎯 Purpose

The main goal of this project is to:

* Help users manage daily tasks digitally
* Provide a structured and interactive CLI experience
* Practice Python programming concepts as a Computer Engineering student
* Implement real-world features like data persistence and task prioritization

---

## 🖥️ User Interface & Menu

When the application starts, users are presented with an interactive menu:

```
1. List Tasks
2. Add New Task
3. Edit / Complete Task
4. Delete Task
5. Sort Tasks
6. Exit
```

### Features:

* **List Tasks** → Displays all tasks in a table format
* **Add Task** → Add task with optional priority and date
* **Edit / Complete** → Update task content or mark as completed
* **Delete Task** → Permanently remove a task
* **Sort Tasks** → Sort tasks based on priority level
* **Exit** → Safely terminate the program

---

## 🛠️ Technical Details

* **Language:** Python
* **Data Storage:** JSON
* **File Handling:** `gorevler.txt` (UTF-8 encoded)
* **Architecture:** Modular function-based design

---

## ⚙️ Key Features

* 📂 **Persistent Data Storage**
  Tasks are saved using the `json` module, ensuring data is not lost between sessions

* ⚠️ **Error Handling**
  Implemented with `try-except` blocks to prevent crashes from invalid input

* 🧩 **Modular Code Structure**
  Each functionality (add, delete, update, etc.) is handled by separate functions

* 🔼 **Priority System**
  Tasks can be assigned:

  * High
  * Medium
  * Low

* 🔃 **Dynamic Sorting**
  Tasks are automatically sorted based on priority levels

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/todo-app.git
```

2. Navigate to the project folder:

```bash
cd todo-app
```

3. Run the application:

```bash
python main.py
```

---

## 📖 Usage Instructions

* Existing tasks are automatically loaded at startup
* Adding a task requires only text input (priority & date are optional)
* Use task ID for editing or deleting tasks
* All changes are instantly saved to the file

---

## 📚 Learning Outcomes

This project demonstrates:

* File handling in Python
* JSON data management
* CLI-based user interaction
* Error handling techniques
* Writing clean and maintainable code

---

## 👩‍💻 Author

**Beyza Karakaya**
Industrial Engineering Student
Interested in software development and problem-solving

---

## 📌 Notes

* This is a **CLI-based application** (no graphical interface)
* Designed for educational and practice purposes
* Can be extended with a GUI (Tkinter / PyQt) or database integration

---

✨ *“Small tools like this build the foundation for bigger systems.”*

## AI USAGE
when this file and project are being prepared, ChatGPT and Gemini Pro versions are used.