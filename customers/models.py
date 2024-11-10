from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_block = models.CharField(max_length=1)
    mode_of_shipment = models.CharField(max_length=10)
    customer_care_calls = models.IntegerField()
    customer_rating = models.IntegerField()
    cost_of_the_product = models.DecimalField(max_digits=10, decimal_places=2)
    prior_purchases = models.IntegerField()
    product_importance = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)  # 'M' or 'F'
    discount_offered = models.IntegerField()
    weight_in_gms = models.IntegerField()
    reached_on_time = models.BooleanField()  # True if delivered on time, False if not

    def __str__(self):
        return f"Customer {self.id}"
