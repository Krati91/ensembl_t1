from django.shortcuts import render
from django.db import connection

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import GeneAutocomplete
# Create your views here.


class GeneSuggest(APIView):
    def get(self, request):
        query_term = "%" + request.GET['query'] + "%"
        query_species = request.GET['species']
        query_limit = int(request.GET['limit'])

        query = 'SELECT display_label FROM gene_autocomplete WHERE display_label LIKE %s AND species=%s LIMIT %s'

        with connection.cursor() as cursor:
            cursor.execute(query, [
                query_term, query_species, query_limit])

            rows = [label[0] for label in cursor.fetchall()]

        return Response(rows, status=status.HTTP_200_OK)
