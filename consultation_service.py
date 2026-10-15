"""In-memory consultation booking service."""

from dataclasses import dataclass


FEES = {"general": 30, "followup": 20}


@dataclass
class Consultation:
    id: int
    patient_name: str
    consultation_type: str
    fee: int
    payment_status: str


class ConsultationService:
    def __init__(self):
        self._consultations = []
        self._next_id = 1

    def create_consultation(self, patient_name, consultation_type, payment_status="unpaid"):
        fee = FEES[consultation_type]
        consultation = Consultation(
            id=self._next_id,
            patient_name=patient_name,
            consultation_type=consultation_type,
            fee=fee,
            payment_status=payment_status,
        )
        self._consultations.append(consultation)
        self._next_id += 1
        return consultation

    def list_consultations(self):
        return list(self._consultations)
