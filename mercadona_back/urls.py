from mercadona_back.views import HomePageBack , SearchProduit
from django.urls import path

urlpatterns = [
    path("", HomePageBack.as_view(), name="home"),
    path("search/", SearchProduit.as_view(), name="search"),
]