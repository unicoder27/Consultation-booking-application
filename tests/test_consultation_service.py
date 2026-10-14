import unittest

from consultation_service import ConsultationService
from reports import list_consultations


class ConsultationServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = ConsultationService()

    def test_creates_general_consultation(self):
        consultation = self.service.create_consultation("Alex Tan", "general")

        self.assertEqual(consultation.id, 1)
        self.assertEqual(consultation.patient_name, "Alex Tan")
        self.assertEqual(consultation.consultation_type, "general")
        self.assertEqual(consultation.fee, 30)
        self.assertEqual(consultation.payment_status, "unpaid")

    def test_creates_followup_consultation(self):
        consultation = self.service.create_consultation("Jamie Lim", "followup")

        self.assertEqual(consultation.fee, 20)

    def test_assigns_sequential_ids_and_stores_consultations(self):
        first = self.service.create_consultation("Alex Tan", "general")
        second = self.service.create_consultation("Jamie Lim", "followup")

        self.assertEqual((first.id, second.id), (1, 2))
        self.assertEqual(len(self.service.list_consultations()), 2)

    def test_report_lists_consultations(self):
        consultation = self.service.create_consultation("Alex Tan", "general")

        self.assertEqual(list_consultations(self.service), [consultation])


if __name__ == "__main__":
    unittest.main()
