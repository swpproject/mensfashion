from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save,post_save
from . models import Product,Category,Order,Cart
from shop.utils import unique_slug_generator_product , unique_slug_generator_category
from django.conf import settings

@receiver(pre_save, sender=Product)
def save_product(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_product(instance)

@receiver(pre_save, sender=Category)
def save_product(sender, instance, *args, **kwarg):
    if not instance.slug:
        instance.slug = unique_slug_generator_category(instance)


@receiver(post_save, sender=Order)
def save_product(sender, instance, *args, **kwarg):
    if instance:
        orderid=instance.id
        user=instance.customer
        msg=Cart.objects.all().filter(customer=user,ordered=False).update(ordered=True,order=orderid)
        print(msg)
