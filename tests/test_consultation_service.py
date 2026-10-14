import unittest

from consultation_service import ConsultationService


class ConsultationServiceTests(unittest.TestCase):
    def test_creates_general_consultation(self):
        service = ConsultationService()

        consultation = service.create_consultation("Alice Tan", "general", "paid")

        self.assertEqual(consultation.id, 1)
        self.assertEqual(consultation.patient_name, "Alice Tan")
        self.assertEqual(consultation.consultation_type, "general")
        self.assertEqual(consultation.fee, 30)
        self.assertEqual(consultation.payment_status, "paid")

    def test_creates_followup_consultation_with_default_payment_status(self):
        service = ConsultationService()

        consultation = service.create_consultation("Bob Lim", "followup")

        self.assertEqual(consultation.fee, 20)
        self.assertEqual(consultation.payment_status, "unpaid")

    def test_stores_consultations_in_memory(self):
        service = ConsultationService()
        first = service.create_consultation("Alice Tan", "general")
        second = service.create_consultation("Bob Lim", "followup")

        self.assertEqual(service.list_consultations(), [first, second])


if __name__ == "__main__":
    unittest.main()
