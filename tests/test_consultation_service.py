import unittest

from consultation_service import (
    clear_consultations,
    create_consultation,
    list_consultations,
)
from reports import consultation_listing


class ConsultationServiceTests(unittest.TestCase):
    def setUp(self):
        clear_consultations()

    def test_creates_general_consultation(self):
        consultation = create_consultation("Alex Tan", "general", "paid")

        self.assertEqual(consultation.id, 1)
        self.assertEqual(consultation.patient_name, "Alex Tan")
        self.assertEqual(consultation.consultation_type, "general")
        self.assertEqual(consultation.fee, 30)
        self.assertEqual(consultation.payment_status, "paid")

    def test_creates_followup_consultation(self):
        consultation = create_consultation("Jamie Lee", "followup")

        self.assertEqual(consultation.fee, 20)
        self.assertEqual(consultation.payment_status, "unpaid")

    def test_stores_multiple_consultations(self):
        create_consultation("Alex Tan", "general")
        create_consultation("Jamie Lee", "followup")

        self.assertEqual(len(list_consultations()), 2)
        self.assertEqual(list_consultations()[1].id, 2)

    def test_listing_reports_stored_consultations(self):
        create_consultation("Alex Tan", "general", "paid")

        self.assertIn("Alex Tan - general (SGD 30, paid)", consultation_listing())


if __name__ == "__main__":
    unittest.main()
