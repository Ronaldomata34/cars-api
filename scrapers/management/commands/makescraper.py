from django.core.management.base import BaseCommand, CommandError
from scrapers.carspider import CarMakeSpider

class Command(BaseCommand):
    help = 'Run makes scraper'

    def handle(self, *args, **options):
        scraper = CarMakeSpider()
        scraper.start_scraper()
        self.stdout.write(self.style.SUCCESS('Successfully scraped'))

"""https://www.cargurus.com/Cars/getCarPickerReferenceDataAJAX.action?forPriceAnalysis=false&showInactive=false&newCarsOnly=false&useInventoryService=true&quotableCarsOnly=false&carsWithRegressionOnly=false&localeCountryCarsOnly=true"""

PARAMS = {
    'forPriceAnalysis':False,
    'showInactive': False,
    'newCarsOnly':False,
    'useInventoryService':True,
    'quotableCarsOnly':False,
    'carsWithRegressionOnly':False,
    'localeCountryCarsOnly':True
    } 