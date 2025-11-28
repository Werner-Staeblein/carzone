from django.apps import AppConfig

from django.db.backends.signals import connection_created
from django.dispatch import receiver

@receiver(connection_created)
def set_timezone(sender, connection, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("SET timezone TO 'UTC';")

class PagesConfig(AppConfig):
    name = 'pages'

