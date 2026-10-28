# Task 3: Authentication and Authorization in a Flask API

## Project Overview
This project implements an Employee Management API using Python and Flask. It provides authentication through login credentials and role-based authorization to protect employee records.

## Features
- User login with valid credentials.
- Token-based authentication for protected endpoints.
- Two roles: Employee and Administrator.
- Employees can view employee records.
- Administrators can view, add, update, and delete employee records.
- Unauthenticated requests are rejected.
- Employees cannot perform administrator-only operations.

## Demo Credentials

| Role | Username | Password |
|---|---|---|
| Employee | employee1 | emp123 |
| Administrator | admin | admin123 |

These credentials are for assignment demonstration only.

## API Endpoints

| Method | Endpoint | Permission |
|---|---|---|
| POST | `/login` | Public |
| GET | `/employees` | Employee, Administrator |
| POST | `/employees` | Administrator |
| PUT | `/employees/<employee_id>` | Administrator |
| DELETE | `/employees/<employee_id>` | Administrator |

## How to Run

1. Install Python and Flask.
2. Open the project folder in VS Code.
3. Run `python -m pip install flask`.
4. Start the API using `python app.py`.
5. The API runs locally at `http://127.0.0.1:5000`.

## Testing

Use cURL or PowerShell to test the endpoints.

- `200 OK`: Request successful.
- `201 Created`: Employee added successfully.
- `400 Bad Request`: Invalid request data.
- `401 Unauthorized`: Missing or invalid authentication credentials.
- `403 Forbidden`: Authenticated user lacks permission.
- `404 Not Found`: Employee record does not exist.

## Authentication vs Authorization

Authentication verifies the user's identity using login credentials and a token. Authorization checks the authenticated user's role before allowing access to restricted operations.

An Employee can view records but receives `403 Forbidden` when attempting administrator-only operations. A request without a valid token receives `401 Unauthorized`.

## Technologies Used
- Python
- Flask
- REST API
- JSON
- PowerShell / cURL

## Note
This is an educational demonstration. Users, tokens, and employee records are stored in memory and reset when the server restarts. A production system should use persistent storage, securely hashed passwords, token expiration, and appropriate secret management.
