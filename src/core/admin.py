from django.contrib import admin

from core.models import CoffeeMachine, CoffeePod, MachineCode, Flavor, PackSize

admin.site.register(CoffeeMachine)
admin.site.register(CoffeePod)

admin.site.register(MachineCode)
admin.site.register(Flavor)
admin.site.register(PackSize)