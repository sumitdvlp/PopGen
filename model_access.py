from django.core.management.base import BaseCommand
from JobSchd.models import JobFinal

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        j=JobFinal.objects.all().count()
        print 'coount',j

    def handle(self, *args, **options):
        self._create_tags()