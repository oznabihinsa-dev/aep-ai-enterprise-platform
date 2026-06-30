from aep.services.commercial.template_repository import TemplateRepository


repo = TemplateRepository("sample_data/templates")

template = repo.find_commercial_offer_template()

print(template)