from flask import Flask, request, jsonify
from functools import wraps
import secrets

app = Flask(__name__)

# Demo users (assignment purposes)
users = {
    "employee1": {
        "password": "emp123",
        "role": "Employee"
    },
    "admin": {
        "password": "admin123",
        "role": "Administrator"
    }
}

# Store active login tokens
tokens = {}

# Sample employee records
employees = [
    {
        "id": 1,
        "name": "Ali Khan",
        "department": "IT"
    },
    {
        "id": 2,
        "name": "Sara Ahmed",
        "department": "HR"
    }
]


# Authentication: user must have a valid token
def authenticate():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization", "")

            if not auth_header.startswith("Bearer "):
                return jsonify({
                    "error": "Authentication required. Please log in."
                }), 401

            token = auth_header.split(" ", 1)[1]
            username = tokens.get(token)

            if not username:
                return jsonify({
                    "error": "Invalid or expired token."
                }), 401

            request.current_user = users[username]
            request.current_username = username

            return func(*args, **kwargs)

        return wrapper
    return decorator


# Authorization: restrict operations by role
def role_required(*allowed_roles):
    def decorator(func):
        @wraps(func)
        @authenticate()
        def wrapper(*args, **kwargs):
            if request.current_user["role"] not in allowed_roles:
                return jsonify({
                    "error": "Forbidden. Administrator access required."
                }), 403
 

            return func(*args, **kwargs)

        return wrapper
    return decorator


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Employee Management API is running"
    })


# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "A valid JSON object is required"
        }), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username) if isinstance(username, str) else None

    if not user or not isinstance(password, str) or not secrets.compare_digest(
        user["password"], password
    ):
        return jsonify({
            "error": "Invalid username or password"
        }), 401

    token = secrets.token_urlsafe(32)
    tokens[token] = username

    return jsonify({
        "message": "Login successful",
        "username": username,
        "role": user["role"],
        "token": token
    }), 200


# View all employee records: Employee and Administrator
@app.route("/employees", methods=["GET"])
@role_required("Employee", "Administrator")
def get_employees():
    return jsonify(employees), 200


# Add employee: Administrator only
@app.route("/employees", methods=["POST"])
@role_required("Administrator")
def add_employee():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "A valid JSON object is required"
        }), 400

    name = data.get("name")
    department = data.get("department")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Valid name is required"}), 400

    if not isinstance(department, str) or not department.strip():
        return jsonify({"error": "Valid department is required"}), 400

    new_employee = {
        "id": max((e["id"] for e in employees), default=0) + 1,
        "name": name.strip(),
        "department": department.strip()
    }

    employees.append(new_employee)

    return jsonify({
        "message": "Employee added successfully",
        "employee": new_employee
    }), 201


# Update employee: Administrator only
@app.route("/employees/<int:employee_id>", methods=["PUT"])
@role_required("Administrator")
def update_employee(employee_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "A valid JSON object is required"
        }), 400

    employee = next(
        (e for e in employees if e["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    name = data.get("name", employee["name"])
    department = data.get("department", employee["department"])

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Valid name is required"}), 400

    if not isinstance(department, str) or not department.strip():
        return jsonify({"error": "Valid department is required"}), 400

    employee["name"] = name.strip()
    employee["department"] = department.strip()

    return jsonify({
        "message": "Employee updated successfully",
        "employee": employee
    }), 200


# Delete employee: Administrator only
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
@role_required("Administrator")
def delete_employee(employee_id):
    employee = next(
        (e for e in employees if e["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    employees.remove(employee)

    return jsonify({
        "message": "Employee deleted successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
