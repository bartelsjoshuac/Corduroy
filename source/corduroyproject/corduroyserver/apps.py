from django.apps import AppConfig

# Only need this one since UI and API are combined, database is seperate.
# I not for anything remember why I added the BigAutoField.  perhaps for the primary key???
class CorduroyserverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'corduroyserver'
