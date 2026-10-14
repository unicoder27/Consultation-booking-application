from consultation_service import ConsultationService
from reports import consultation_listing


def main():
    service = ConsultationService()
    service.create_consultation("Alice Tan", "general", "paid")
    service.create_consultation("Bob Lim", "followup")
    print(consultation_listing(service.list_consultations()))


if __name__ == "__main__":
    main()
