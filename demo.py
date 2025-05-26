from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Patient(BaseModel):
    id: int
    name: str
    age: int
    condition: str
    created_at: datetime

patients : List[Patient] = []

@app.get("/")
def read_root():
    return {"Message":"Hello Patient!"}

@app.get("/patients")
def read_patient(condition : Optional[str] = None):
    if condition:
        filtered = [patient for patient in patients if patient.condition.lower() == condition.lower()]
        return filtered
    return patients

@app.post("/patients")
def write_patient(patientValue: Patient):
    patients.append(patientValue)
    return patientValue

@app.put("/patients/{patient_id}")
def update_patient(updated_patient: Patient, patient_id: int):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            patients[index] = updated_patient
            return updated_patient
    return {"Error":"Unable to update patient data!"}

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            deleted = patients.pop(index)
            return deleted
    return {"Error":"Unable to delete!"}








