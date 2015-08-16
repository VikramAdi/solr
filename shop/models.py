from django.db import models
from address.models import Address
from uuid import uuid4
from categories.models import Catalog
from django.template.defaultfilters import slugify

# Create your models here.
def upload_path(instance, filename):
    return '/'.join('shop',instance.name,'docs',instance.field_name)

class Shop(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    name = models.CharField(max_length= 50)
    slug = models.SlugField(max_length = 20, blank = True)
    pin_code = models.CharField(max_length = 6)
    address_line = models.CharField(max_length= 150)
    delivery_areas = models.ManyToManyField(Address, blank = True, null = True)
    served_categories = models.ManyToManyField(Catalog)
    products = models.ManyToManyField('products.Product')
    shop_registration_no = models.CharField(max_length=50)
    shop_registration_img = models.ImageField(upload_to = upload_path,blank=True, null=True)
    tin_no = models.CharField(max_length= 50, blank=True, null=True)
    tin_img = models.ImageField(upload_to = upload_path,null =True, blank = True)
    pan_no = models.CharField(max_length= 13)
    pan_img = models.ImageField(upload_to = upload_path, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    
    def __unicode__(self):
        return '%s at %s' %(self.name, self.address_line)
    
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        slug_words = "%s" %(self.name)
        self.slug = slugify(slug_words)
        super(Shop, self).save()