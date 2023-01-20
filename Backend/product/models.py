

from django.db import models
from .utils import create_uuid

# Create your models here.


class Product(models.Model):
    """
    A class to represent a product that a person is selling.

    ...

    Attributes
    ----------
    description : str
        Description of the product being sold
    pub_date : date
        Date that the product was published
    price : int
        Price that the product is being sold for
    uuid : char
        Str that is meant to be used for front-facing purposes (ex : URL)

    Methods
    -------
    """

    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    uuid = models.CharField(default=create_uuid, unique=True, max_length=6)


    def __str__(self):
        return self.description

