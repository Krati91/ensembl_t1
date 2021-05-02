from django.urls import path
from .views import GeneSuggest

urlpatterns = [
    path('gene_suggest', GeneSuggest.as_view(), name='gene_suggest')
]
