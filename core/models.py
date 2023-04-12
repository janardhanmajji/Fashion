from django.db import models
from django.contrib.auth.models import User
from item.models import Item


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} ({self.quantity})"

    def get_total(self):
        return self.item.price * self.quantity
