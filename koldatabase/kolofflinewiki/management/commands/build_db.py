from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

import sys

sys.path.append('data/')
import build

class Command(BaseCommand):
	def handle(self, *args, **options):
		print('test')
		call_command('makemigrations', 'kolofflinewiki')
		call_command('migrate')

		build.build_db()
