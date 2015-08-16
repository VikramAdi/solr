from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from categories.models import Catalog

# Create your views here.
class CatalogCreate(CreateView, SuccessMessageMixin):
    model = Catalog
    fields = ['name','description',]
    success_message = "Successfully added the catalog"