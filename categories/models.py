from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length= 50)
    slug = models.SlugField(max_length = 20, blank = True )
    publisher = models.ForeignKey(User, editable = False, null =True)
    description = models.TextField(null=True, blank =True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        self.slug = slugify(self.name)
        super(Catalog, self).save()