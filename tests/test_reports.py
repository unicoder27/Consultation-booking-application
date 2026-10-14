import unittest

from consultation_service import ConsultationService
from reports import consultation_listing


class ConsultationReportTests(unittest.TestCase):
    def test_lists_consultation_details(self):
        service = ConsultationService()
        service.create_consultation("Alice Tan", "general", "paid")

        report = consultation_listing(service.list_consultations())

        self.assertEqual(report, "1: Alice Tan - general - SGD 30 - paid")


if __name__ == "__main__":
    unittest.main()
