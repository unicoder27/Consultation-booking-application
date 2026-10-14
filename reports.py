def consultation_listing(consultations):
    """Return a simple text listing of consultations."""
    lines = []
    for consultation in consultations:
        lines.append(
            f"{consultation.id}: {consultation.patient_name} - "
            f"{consultation.consultation_type} - SGD {consultation.fee} - "
            f"{consultation.payment_status}"
        )
    return "\n".join(lines)
