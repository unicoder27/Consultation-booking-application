"""Basic consultation listing."""


def consultation_listing(consultations):
    return [
        f"{item.id}: {item.patient_name} - {item.consultation_type} "
        f"(SGD {item.fee}, {item.payment_status})"
        for item in consultations
    ]
