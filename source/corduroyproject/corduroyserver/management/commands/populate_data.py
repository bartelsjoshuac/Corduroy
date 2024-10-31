from django.core.management.base import BaseCommand
from corduroyserver.models import Trails, Reports
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate sample data for Trails and Reports models'

    def handle(self, *args, **kwargs):
        # Create sample Trails
        trail1, created = Trails.objects.get_or_create(
            trailName="Shrine Pass",
            location="Front Range",
            rating=3
        )
        trail2, created = Trails.objects.get_or_create(
            trailName="Owl Creek Road",
            location="San Juans",
            rating=4
        )

        # Create sample Reports
        Reports.objects.get_or_create(
            approvalStatus=True,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail1,
            report="The shrine looks good."
        )
        Reports.objects.get_or_create(
            approvalStatus=False,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail2,
            report="More owls than ever"
        )

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully'))