# Generated by Django 3.2.16 on 2023-01-20 17:08

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=22, max_length=22, prefix='', primary_key=True, serialize=False, unique=True),
        ),
    ]