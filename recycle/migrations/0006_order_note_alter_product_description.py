# Generated by Django 4.0.3 on 2022-04-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0005_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]