# These aren't working I dunno need to look at it more  Maybe because the ci.yml Github mnade doesn't do postgres?

from django.test import TestCase
from .models import Trails, Reports
from django.utils import timezone

class TrailsAndReportsModelTest(TestCase):
    def setUp(self):
        # Create a sample Trail object
        self.trail = Trails.objects.create(
            trailName="Front Range Trail",
            location="Front Range",
            rating=5
        )

        # Create a sample Report object associated with the Trail
        self.report = Reports.objects.create(
            approvalStatus=False,
            date=timezone.now().date(),
            groomer="John Doe",
            trail=self.trail,
            report="Initial grooming report for Front Range Trail"
        )

    # Trail Tests
    def test_trail_creation(self):
        # Verify that the Trail object was created correctly
        trail = Trails.objects.get(trailName="Front Range Trail")
        self.assertEqual(trail.trailName, "Front Range Trail")
        self.assertEqual(trail.location, "Front Range")
        self.assertEqual(trail.rating, 5)

    def test_trail_update(self):
        # Test updating a Trail's rating
        self.trail.rating = 4
        self.trail.save()
        updated_trail = Trails.objects.get(id=self.trail.id)
        self.assertEqual(updated_trail.rating, 4)

    def test_trail_deletion(self):
        # Verify that deleting a Trail also removes associated Reports
        trail_id = self.trail.id
        self.trail.delete()
        with self.assertRaises(Trails.DoesNotExist):
            Trails.objects.get(id=trail_id)
        # Ensure related Report is also deleted
        with self.assertRaises(Reports.DoesNotExist):
            Reports.objects.get(id=self.report.id)

    # Report Tests
    def test_report_creation(self):
        # Verify that the Report object was created correctly and is linked to the Trail
        report = Reports.objects.get(report="Initial grooming report for Front Range Trail")
        self.assertEqual(report.trail, self.trail)
        self.assertEqual(report.groomer, "John Doe")
        self.assertFalse(report.approvalStatus)

    def test_report_update(self):
        # Test updating a Report's approval status
        self.report.approvalStatus = True
        self.report.save()
        updated_report = Reports.objects.get(id=self.report.id)
        self.assertTrue(updated_report.approvalStatus)

    def test_report_deletion(self):
        # Verify that a Report can be deleted without affecting the associated Trail
        report_id = self.report.id
        self.report.delete()
        with self.assertRaises(Reports.DoesNotExist):
            Reports.objects.get(id=report_id)
        # Ensure the Trail still exists
        self.assertTrue(Trails.objects.filter(id=self.trail.id).exists())

   #def test_fail_on_purpose(self):
   #     self.assertEqual(1, 0, "Intentional failure to test CI pipeline")