from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict
from typing import List, Optional

app = Flask(__name__)

@dataclass
class Patient:
    user_id: int
    name: str
    medicines: str
    amount: int

users: List[Patient] = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello User!"})

@app.route("/users", methods=["GET"])
def get_users():
    name = request.args.get("name")
    if name:
        filtered = [asdict(patient) for patient in users if patient.name.lower() == name.lower()]
        return jsonify(filtered)
    return jsonify([asdict(patient) for patient in users])

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_patient = Patient(**data)
    users.append(new_patient)
    return jsonify(asdict(new_patient)), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    for index, patient in enumerate(users):
        if patient.user_id == user_id:
            users[index] = Patient(**data)
            return jsonify(asdict(users[index]))
    return jsonify({"error": "Patient Not Found"}), 404

@app.route("/users/<int:patient_id>", methods=["DELETE"])
def delete_user(patient_id):
    for index, patient in enumerate(users):
        if patient.user_id == patient_id:
            deleted = users.pop(index)
            return jsonify({"message": f"Deleted Successfully! for {deleted.name}"})
    return jsonify({"error": "Patient Not Found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
