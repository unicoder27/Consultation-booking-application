from consultation_service import ConsultationService
from reports import list_consultations


def main():
    service = ConsultationService()
    service.create_consultation("Alex Tan", "general")
    service.create_consultation("Jamie Lim", "followup")

    for consultation in list_consultations(service):
        print(
            f"{consultation.id}: {consultation.patient_name} - "
            f"{consultation.consultation_type} (SGD {consultation.fee}), "
            f"{consultation.payment_status}"
        )


if __name__ == "__main__":
    main()
