# Generated by Django 5.1.3 on 2024-11-08 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_block', models.CharField(max_length=1)),
                ('mode_of_shipment', models.CharField(max_length=10)),
                ('customer_care_calls', models.IntegerField()),
                ('customer_rating', models.IntegerField()),
                ('cost_of_the_product', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prior_purchases', models.IntegerField()),
                ('product_importance', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('discount_offered', models.IntegerField()),
                ('weight_in_gms', models.IntegerField()),
                ('reached_on_time', models.BooleanField()),
            ],
        ),
    ]