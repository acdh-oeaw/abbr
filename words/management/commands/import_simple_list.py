import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from words.utils import save_simple_abbr_list

cwd = settings.BASE_DIR


class Command(BaseCommand):
    # Show this when the user types help
    help = "Imports abbrevation from a text file with one abbrevation per line"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    # A command must define handle()
    def handle(self, *args, **options):
        try:
            file = options['file']
        except KeyError:
            file = None

        if file:
            stored = save_simple_abbr_list(file)
            saved_items = len(stored[0])
            self.stdout.write('{} items imported'.format(saved_items))
        else:
            self.stdout.write('provide a file name')
