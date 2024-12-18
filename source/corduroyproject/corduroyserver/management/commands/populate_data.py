# This should be run after the populate_user.py or we run into data integrity issues.
#  It creates some trails and some reports, two are approved already (which is not the default in the model) and the rest are not approved.  Giving someone change to play both user types.
#  It is intended for deploying the application in a demonstration only.

from django.core.management.base import BaseCommand
from corduroyserver.models import Trails, Reports
# For the date.now() 
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate sample data for Trails and Reports models'

    def handle(self, *args, **kwargs):
        # Create sample Trails
        trail1, created = Trails.objects.get_or_create(
            trailName="Shrine Pass",
            location="Front Range",
            rating=1
        )
        trail2, created = Trails.objects.get_or_create(
            trailName="Owl Creek Road",
            location="San Juans",
            rating=2
        )
        trail3, created = Trails.objects.get_or_create(
            trailName="Sunlight",
            location="Grand Mesa",
            rating=3
        )
        trail4, created = Trails.objects.get_or_create(
            trailName="Lake Loop",
            location="Grand Lake",
            rating=3
        )
        trail5, created = Trails.objects.get_or_create(
            trailName="Snowy Mountains FSA",
            location="Other",
            rating=7
        )

        # Create sample Reports
        Reports.objects.get_or_create(
            approvalStatus=True,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail1,
            report="More Shrines than normal."
        )
        Reports.objects.get_or_create(
            approvalStatus=True,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail2,
            report="Less Owls than normal."
        )
        Reports.objects.get_or_create(
            approvalStatus=False,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail3,
            report="More sunny than normal."
        )
        Reports.objects.get_or_create(
            approvalStatus=False,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail4,
            report="Less grand than normal."
        )
        Reports.objects.get_or_create(
            approvalStatus=False,
            date=timezone.now().date(),
            groomer="groomy",
            trail=trail5,
            report="More snowy than normal."
        )
          
        self.stdout.write(self.style.SUCCESS('Sample data populated successfully'))