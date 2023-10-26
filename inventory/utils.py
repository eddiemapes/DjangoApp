from .models import *

def assign_total(purchase):
        purchase.purchase.price = purchase.purchase.menu_item.price
        purchase.purchase.price.save()