from django.contrib import admin


from .models import Product,Category,New

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(New)
