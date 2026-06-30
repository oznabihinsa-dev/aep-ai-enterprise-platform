from aep.services.commercial.certificate_repository import CertificateRepository


repo = CertificateRepository("sample_data/certificates")

certificate = repo.find_certificate("2БПК")

print(certificate)