from django.core.management.base import BaseCommand, CommandError
from scrapers.carspider import CarMakeSpider

class Command(BaseCommand):
    help = 'Run makes scraper'

    def handle(self, *args, **options):
        scraper = CarMakeSpider()
        scraper.start_scraper()
        self.stdout.write(self.style.SUCCESS('Successfully scraped'))