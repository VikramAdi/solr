from django.db import models
from categories.models import Catalog
from uuid import uuid4
from shop.models import Shop
from django.template.defaultfilters import slugify

# Create your models here.
def upload_path(instance, filename):
    return '/'.join(instance.shop, instance.category, instance.name)

class Product(models.Model):
    id = models.UUIDField(default= uuid4, unique=True, primary_key = True, editable = False)
    name = models.CharField(max_length= 30)
    slug = models.SlugField(max_length = 20, blank = True)
    category = models.ForeignKey(Catalog)
    synonym_1 = models.CharField(max_length = 30, blank = True)
    synonym_2 = models.CharField(max_length = 30, blank = True)
    synonym_3 = models.CharField(max_length = 30, blank = True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.slug = slugify(self.name)
        super(Product, self).save()

class ProductSpecs(Product):
    frnd_name = models.CharField("common name", max_length= 30,)
    scientific_name = models.CharField(max_length = 50, blank = True, null = True)
    description = models.TextField()
    
class ProductPic(models.Model):
    product = models.ForeignKey(Product)
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length = 50, blank = True, null = True)
    pic = models.ImageField(upload_to = upload_path, null = True)
    