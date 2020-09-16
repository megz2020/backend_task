from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _


MACHUNE_TYPE =(
        ('COFFEE_MACHINE_LARGE', 'large machine'),
        ('COFFEE_MACHINE_SMALL', 'small machine'),
        ('ESPRESSO_MACHINE', 'espresso machine'),
    )

MACHINE_MODELS =(
        ('BASE', 'base model'),
        ('PREMIUM', 'premium model'),
        ('DELUXE', 'deluxe model'),
    )

PODS_TYPES = (
        ('COFFEE_POD_LARGE', 'large coffee pod'),
        ('COFFEE_POD_SMALL', 'small coffee pod'),
        ('ESPRESSO_POD', 'espresso pod'),
    )

FLAVORS = (
        ('COFFEE_FLAVOR_VANILLA', "vanilla"),
        ('COFFEE_FLAVOR_CARAMEL', "caramel"),
        ('COFFEE_FLAVOR_PSL', "psl"),
        ('COFFEE_FLAVOR_MOCHA', "mocha"),
        ('COFFEE_FLAVOR_HAZELNUT', "hazelnut"),
    )
PACK_SIZE = (
        ('DOZEN_1', '1 dozen'),
        ('DOZEN_3', '3 dozen'),
        ('DOZEN_5', '5 dozen'),
        ('DOZEN_7', '7 dozen')
    )


class MachineCode(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class Flavor(models.Model):
    flavor = models.CharField(max_length=100, null=False, 
    blank=False, unique=True, choices=FLAVORS)

    def __str__(self):
        return self.flavor


class PackSize(models.Model):
    pack_size = models.CharField(max_length=20, choices=PACK_SIZE)

    def __str__(self):
        return self.pack_size

class CoffeePod(models.Model):
    product_type = models.CharField(max_length=255, choices=PODS_TYPES, null=False, blank=False)

    sku_code = models.ForeignKey(MachineCode, null=True, blank=False, on_delete=models.SET_NULL,
                                     related_name="sku")
    coffee_flavor = models.ForeignKey(Flavor, null=True, blank=True,
                                      on_delete=models.SET_NULL)
    pack_size = models.ForeignKey(PackSize, null=True, blank=True,
                                  on_delete=models.SET_NULL)
                                  
 

    def __str__(self):
        return self.sku_code.code





class CoffeeMachine(models.Model):
    product_type = models.CharField(max_length=255, choices=MACHUNE_TYPE, null=False, blank=False)
    model = models.CharField(max_length=255, choices=MACHINE_MODELS, null=False, blank=False)


    sku_code = models.ForeignKey(MachineCode, null=True,  blank=False,related_name="code_machine" ,on_delete=models.SET_NULL)
    pod = models.ForeignKey(CoffeePod, null=True, blank=True,related_name="pod" ,on_delete=models.SET_NULL)
    water_line_compatible = models.BooleanField(default=False)

    def __str__(self):
        return self.sku_code.code





# def your_receiver_function(sender, instance, *args, **kwargs):
#       if instance.title and not instance.slug:
#                instance.slug = slugify(instance.title)

# pre_save.connect(your_receiver_function, sender=YourModel)`
