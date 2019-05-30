from django.db import models
from django.utils import timezone

shippng_method = (
    ('0414', 'SEDEX'),
    ( '04510', 'PAC'),
    ('0215', 'SEDEX10'),
)

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    purchase_itens = models.ForeignKey('Product', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default = timezone.now)
    tracking_code = models.CharField(max_length = 40)
    purchase_amount = models.DecimalField(max_digits=5, decimal_places=2)
    tracking_mode = models.CharField(max_length = 6, choices=shippng_method)
    shippng_time = models.CharField(max_length = 2)
    
    def save_purchase(self):
        self.purchase_date = timezone.now
        self.save()

    def __str__(self):
       return 'Compra nº ' + str(self.purchase_id)

class Product(models.Model):
    product_description = models.CharField(max_length=200)
    product_cost = models.DecimalField(max_digits=20, decimal_places=2)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_weight = models.DecimalField(max_digits=20, decimal_places=2)
    product_width = models.DecimalField(max_digits=20, decimal_places=2)
    product_length = models.DecimalField(max_digits=20, decimal_places=2)
    product_id = models.AutoField(primary_key=True)
    produtc_status = models.CharField(max_length = 40)
    product_quantity = models.IntegerField()

    def save_product(self):
        self.save()
    
    def __str__(self):
        return self.product_description