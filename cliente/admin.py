from django.contrib import admin


from .models import Cliente
from .models import Ventas

admin.site.register(Cliente)

admin.site.register(Ventas)

# Register your models here.
