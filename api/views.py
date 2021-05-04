# File for api requests processing

from django.shortcuts import render

from rest_framework.views import APIView

from .utils import error_prompt, get_rows
# Create your views here.


class GeneSuggest(APIView):
    def get(self, request):
        '''
        To return the list of display labels as per the values passed in query, species and limit request parameters.
        '''
        try:
            query_term = "%" + request.GET['query'] + "%"
            query_species = request.GET['species']
            query_limit = int(request.GET['limit'])
        except Exception as e:
            return error_prompt(e)

        query = 'SELECT display_label FROM gene_autocomplete WHERE display_label LIKE %s AND species=%s LIMIT %s'

        query_response = get_rows(
            query, query_term, query_species, query_limit)

        return query_response
