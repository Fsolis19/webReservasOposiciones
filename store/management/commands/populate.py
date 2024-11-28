# store/management(commands/populate.py)

from django.core.management.base import BaseCommand
from store.models import Status, Order, OrderItem
import random

class Command(BaseCommand):
    help = 'Populate database with test data'

    def handle(self, *args, **options):
        # Delete all
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        Status.objects.all().delete()

        # Create all Status
        status1, created = Status.objects.get_or_create(name='No realizado')
        status2, created = Status.objects.get_or_create(name='Realizado')
        status3, created = Status.objects.get_or_create(name='Gestionado')
        status4, created = Status.objects.get_or_create(name='Enviado')
        status5, created = Status.objects.get_or_create(name='En reparto')
        status6, created = Status.objects.get_or_create(name='Entregado')
        status7, created = Status.objects.get_or_create(name='Cancelado')
        status8, created = Status.objects.get_or_create(name='Devuelto')        
