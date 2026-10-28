# Software Engineering Assignment 1

A collection of three practical Software Engineering tasks developed using Python and Flask. This repository demonstrates REST API development, API key authentication, database integration, and role-based access control.

## 📌 Project Overview

This assignment consists of three tasks:

1. **Task 1: Student Management Database API**
2. **Task 2: API Key Authentication**
3. **Task 3: Authentication and Authorization API**

Each task is organized in a separate folder with its source code and relevant documentation.

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- Streamlit
- REST APIs
- JSON
- PowerShell
- Git and GitHub

## 📂 Repository Structure

```text
Software-Engineering-Assignment-1/
│
├── Task_1_Database_API_StreamLit/
│   ├── app.py
│   ├── streamlit_app.py
│   ├── README.md
│   └── students.db
│
├── Task_2_API_Key_Authentication/
│   ├── app.py
│   └── README.md
│
├── Task_3_Authentication_Authorization_API/
│   ├── app.py
│   └── README.md
│
├── .gitignore
└── README.md
```

*Note: The filenames shown above are examples. The actual structure may differ slightly depending on the files in each task folder.*

---

## 🚀 Task 1: Student Management Database API

**Objective:** Develop a Flask API connected to an SQLite database and a Streamlit interface for managing student records.

### Key Features

- Retrieve student records through a REST API.
- Store and manage data using SQLite.
- Perform student record operations.
- Provide a user-friendly interface using Streamlit.

**Technologies:** Python, Flask, SQLite, Streamlit.

### 🎥 Demo Video

**Demo Video:** [Add Task 1 Demo Video Link Here] https://youtu.be/a8-3bCTTTiI?si=N-yqxRYcqj9cT98o

---

## 🔐 Task 2: API Key Authentication

**Objective:** Implement API key-based authentication to protect an API endpoint from unauthorized access.

### Key Features

- Generate and use an API key.
- Validate API keys in incoming requests.
- Allow authorized requests.
- Reject requests with missing or invalid API keys.

**Technologies:** Python, Flask, REST API, HTTP headers.

### 🎥 Demo Video

**Demo Video:** [Add Task 2 Demo Video Link Here] https://youtu.be/3YzAyzM2fOM?si=EWswGnbHN8hXupJm

---

## 🛡️ Task 3: Authentication and Authorization API

**Objective:** Develop an employee management API that uses login tokens for authentication and role-based permissions for authorization.

### Key Features

- User login and token generation.
- Bearer token authentication.
- Employee and Administrator roles.
- View, add, update, and delete employee records.
- HTTP 401 response for unauthenticated requests.
- HTTP 403 response for unauthorized operations.

**Technologies:** Python, Flask, REST API, JSON, PowerShell.

### 🎥 Demo Video

**Demo Video:** 
[Add Task 3 Demo Video Link Here] https://youtu.be/eL9waQmy7fA
---

## ▶️ How to Run the Projects

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Software-Engineering-Assignment-1
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required packages for the specific task. For example:

```bash
pip install flask streamlit
```

Install any additional dependencies required by the individual task.

### 4. Run the API

Open the relevant task folder and run:

```bash
python app.py
```

For Task 1, if the Streamlit interface is required, open another terminal and run:

```bash
streamlit run streamlit_app.py
```

Refer to each task's folder for any task-specific setup instructions.

---

## 📚 Learning Outcomes

Through these tasks, I practiced:

- Designing and testing REST APIs.
- Integrating Flask applications with databases.
- Implementing API key authentication.
- Working with login tokens and role-based authorization.
- Testing API endpoints using PowerShell.
- Organizing projects and documenting code with GitHub.

## 👨‍💻 Author

**Abdul Mannio Hulio**
**BS Computer Science** 
**Undergraduate**

Software Engineering Assignment 1

## 📄 Disclaimer
These projects were developed for educational and demonstration purposes. Security-sensitive implementations should be strengthened before production use.
