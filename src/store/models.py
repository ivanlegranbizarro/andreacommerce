from django.db import models

# Create your models here.

CHANNEL_CHOICES = (
    ('W', 'WallaPop'),
    ('I', 'Instagram'),
    ('O', 'Otros...')
)


class Customer(models.Model):
    customer = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f'Nombre: {self.customer} | Email: {self.email}'


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}. Id Order: {self.id}'

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()

        return self.get_total_item_price()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    shipping_address = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    channels = models.CharField(choices=CHANNEL_CHOICES, max_length=1)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def __str__(self):
        return f'ID: {self.id} | Factura de {self.customer}.'
