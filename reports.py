"""Basic consultation listing report."""

from consultation_service import list_consultations


def consultation_listing():
    """Return a readable listing of all consultations."""
    consultations = list_consultations()
    if not consultations:
        return "No consultations booked."

    lines = ["Consultations:"]
    for item in consultations:
        lines.append(
            f"{item.id}. {item.patient_name} - {item.consultation_type} "
            f"(SGD {item.fee}, {item.payment_status})"
        )
    return "\n".join(lines)
