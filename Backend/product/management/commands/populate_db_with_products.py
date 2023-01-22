import random
import string

from django.core.management import BaseCommand
from django.utils import timezone
from ...models import Product

class Command(BaseCommand):

    help = "Populates product database with 100 random entries"

    def handle(self, *args, **options):

        for i in range(100):
            rand_desc = '' + random.choice(string.ascii_uppercase) + ''.join(
                [random.choice(string.ascii_lowercase) for i in range(6)])

            rand_price = round(random.uniform(0, 999),2)

            product = Product.objects.create(
                description=rand_desc,
                pub_date=timezone.now(),
                price=rand_price
            )

            product.save()
