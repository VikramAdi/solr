from haystack import indexes
from models import Catalog

class CatalogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template = True)
    cat_name = indexes.CharField(model_attr = 'name')
    
    def get_model(self):
        return Catalog
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()