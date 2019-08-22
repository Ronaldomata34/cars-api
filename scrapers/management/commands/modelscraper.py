from django.core.management.base import BaseCommand, CommandError
from scrapers.carspider import CarModelSpider

class Command(BaseCommand):
    help = 'Run models scraper'

    def handle(self, *args, **options):
        scraper = CarModelSpider()
        scraper.start_scraper()
        self.stdout.write(self.style.SUCCESS('Successfully scraped'))