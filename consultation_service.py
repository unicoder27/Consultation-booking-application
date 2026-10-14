"""Simple in-memory consultation booking service."""

from dataclasses import dataclass
from itertools import count


FEES = {"general": 30, "followup": 20}


@dataclass
class Consultation:
    id: int
    patient_name: str
    consultation_type: str
    fee: int
    payment_status: str


_consultations = []
_next_id = count(1)


def create_consultation(patient_name, consultation_type, payment_status="unpaid"):
    """Create and store a consultation, returning the new record."""
    fee = FEES[consultation_type]
    consultation = Consultation(
        id=next(_next_id),
        patient_name=patient_name,
        consultation_type=consultation_type,
        fee=fee,
        payment_status=payment_status,
    )
    _consultations.append(consultation)
    return consultation


def list_consultations():
    """Return a copy of the consultations stored in memory."""
    return list(_consultations)


def clear_consultations():
    """Clear stored records and restart IDs (useful for isolated examples/tests)."""
    global _next_id
    _consultations.clear()
    _next_id = count(1)
