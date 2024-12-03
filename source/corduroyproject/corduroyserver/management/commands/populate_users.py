# This create two groups, one for admins (admins) and one for groomers (groomers)  
# It creates two users, groomy and admin and adds them to the obvious associated group
# This admin user and group is not the Django admin user or group, which will be root.
# It also assumes you used root in your createsuper command and adds root to both groups as otherwise even root can not get to the pages
# This is likely a more elegant way to determine who the superuser proglamatically and add them however it seems to always be root.
# Probably with no Admin URL you would disable the root in a production enviroment anyway?
# It is intended for deploying the application in a demonstration only

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from corduroyserver.models import Trails, Reports

class Command(BaseCommand):
    help = 'Populate sample users, add them to specific groups with permissions, and add root to both groups'

    def handle(self, *args, **kwargs):
        # Create groups
        groomers_group, created = Group.objects.get_or_create(name='groomers')
        admins_group, created = Group.objects.get_or_create(name='admins')

        # Set permissions for the admins group
        if created:
            # Grant admins full permissions on Trails and Reports models
            trails_permissions = Permission.objects.filter(content_type__app_label='corduroyserver', codename__icontains='trails')
            reports_permissions = Permission.objects.filter(content_type__app_label='corduroyserver', codename__icontains='reports')
            admins_group.permissions.set(trails_permissions | reports_permissions)
        
        # Set permissions for the groomers group
        report_content_type = ContentType.objects.get_for_model(Reports)
        groomers_permissions = Permission.objects.filter(
            content_type=report_content_type, codename__in=['add_reports', 'change_reports']
        )
        groomers_group.permissions.set(groomers_permissions)

        # Create sample users and assign them to the groups
        user1, created = User.objects.get_or_create(username='groomy', email='groomer@example.com')
        if created:
            user1.set_password('password')
            user1.groups.add(groomers_group)
            user1.save()

        user2, created = User.objects.get_or_create(username='admin', email='admin@example.com')
        if created:
            user2.set_password('password')
            user2.groups.add(admins_group)
            user2.save()

        # This account is only used for testing lack of access to functions that require group access
        user3, created = User.objects.get_or_create(username='nobody', email='nobody@example.com')
        if created:
            user3.set_password('password')
            user3.save()

        # Add the existing 'root' user to both groups if root exists (it has to as we assumed so as note in top comments)
        try:
            root_user = User.objects.get(username='root')
            root_user.groups.add(groomers_group, admins_group)
            root_user.save()
            self.stdout.write(self.style.SUCCESS("Root user added to groomers and admins groups"))
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING("Root user does not exist; run python manage.py createsuperuser to create root"))

        self.stdout.write(self.style.SUCCESS('Users, groups, permissions, and root assignments created successfully'))

