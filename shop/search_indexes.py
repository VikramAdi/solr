from haystack import indexes
from models import Shop
from django.utils import timezone

class ShopIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template = True)
    shop_name = indexes.CharField(model_attr = 'name')
    shop_pin = indexes.CharField(model_attr = 'pin_code')
    served_categories = indexes.CharField(model_attr = 'served_categories')
    updated_on = indexes.DateTimeField(model_attr = 'updated_on')
    
    def get_model(self):
        return Shop
    
    def prepare_reg_cat(self,obj):
        return [served_categories.name for served_categories in obj.served_categories.all()]
    
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(updated_on__lte=timezone.now())