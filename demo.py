"""Run a small consultation-booking example."""

from consultation_service import create_consultation
from reports import consultation_listing


def main():
    create_consultation("Alex Tan", "general", "paid")
    create_consultation("Jamie Lee", "followup")
    print(consultation_listing())


if __name__ == "__main__":
    main()
