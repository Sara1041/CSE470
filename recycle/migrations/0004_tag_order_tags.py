# Generated by Django 4.0.3 on 2022-04-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0003_order_customer_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='recycle.tag'),
        ),
    ]
