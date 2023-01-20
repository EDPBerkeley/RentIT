from django.utils import timezone
import random
import string

from product.models import Product

rand_desc = '' + random.choice(string.ascii_uppercase) + ''.join([random.choice(string.ascii_lowercase) for i in range(6)])
rand_price = random.randint(0,100)
p = Product.objects.create(
    description=rand_desc,
    pub_date=timezone.now(),
    price=rand_price
)
p.save()
