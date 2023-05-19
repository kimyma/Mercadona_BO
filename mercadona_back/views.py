
from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from mercadona_back.models import Produit


# Create your views here.
class HomePageBack(TemplateView):
    template_name = 'home.html'

class SearchProduit(ListView):
    model = Produit
    template_name = 'search.html'