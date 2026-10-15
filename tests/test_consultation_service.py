import unittest

from consultation_service import ConsultationService
from reports import consultation_listing


class ConsultationServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = ConsultationService()

    def test_creates_general_consultation(self):
        item = self.service.create_consultation("Alex Tan", "general")
        self.assertEqual(item.id, 1)
        self.assertEqual(item.patient_name, "Alex Tan")
        self.assertEqual(item.consultation_type, "general")
        self.assertEqual(item.fee, 30)
        self.assertEqual(item.payment_status, "unpaid")

    def test_followup_fee_and_paid_status(self):
        item = self.service.create_consultation("Jamie Lee", "followup", "paid")
        self.assertEqual(item.fee, 20)
        self.assertEqual(item.payment_status, "paid")

    def test_consultations_are_stored_with_incrementing_ids(self):
        first = self.service.create_consultation("Alex", "general")
        second = self.service.create_consultation("Jamie", "followup")
        self.assertEqual([item.id for item in self.service.list_consultations()], [1, 2])
        self.assertIs(self.service.list_consultations()[0], first)
        self.assertIs(self.service.list_consultations()[1], second)

    def test_basic_listing(self):
        self.service.create_consultation("Alex Tan", "general")
        self.assertEqual(
            consultation_listing(self.service.list_consultations()),
            ["1: Alex Tan - general (SGD 30, unpaid)"],
        )


if __name__ == "__main__":
    unittest.main()
