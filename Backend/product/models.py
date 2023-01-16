from django.db import models

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

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.description



