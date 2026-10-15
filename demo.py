"""Runnable example of booking and listing consultations."""

from consultation_service import ConsultationService
from reports import consultation_listing


def main():
    service = ConsultationService()
    service.create_consultation("Alex Tan", "general")
    service.create_consultation("Jamie Lee", "followup", payment_status="paid")
    print("Consultations:")
    for line in consultation_listing(service.list_consultations()):
        print(line)


if __name__ == "__main__":
    main()
