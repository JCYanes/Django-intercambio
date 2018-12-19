from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    img = models.CharField(max_length=256, blank=True, null=True)
    active = models.BooleanField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256, blank=True, null=True)
    year = models.IntegerField( blank=True, null=True)
    new  = models.BooleanField()
    price = models.IntegerField()
    barter = models.BooleanField()
    img = models.CharField(max_length=256, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.title



class New(models.Model):
    title = models.CharField(max_length=256,blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    year = models.IntegerField( blank=True, null=True)
    author  = models.CharField(max_length=256,blank=True, null=True)

    def __str__(self):
        return self.title
