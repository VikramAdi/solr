from haystack import indexes
from models import ProductSpecs

class ProductSpecsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template = True)
    grain_name = indexes.CharField(model_attr = 'name')
    grain_cast = indexes.CharField(model_attr = 'frnd_name')
    
    def get_model(self):
        return ProductSpecs
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()