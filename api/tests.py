from django.test import TestCase

from rest_framework.test import APIRequestFactory

from .views import GeneSuggest
# Create your tests here.

factory = APIRequestFactory()
view = GeneSuggest.as_view()

# Test Case 1
params = {
    'query': 'brc',
    'species': 'homo_sapiens',
    'limit': '10'
}

request = factory.get('/gene_suggest/', params)
response = view(request)

assert(response.status_code == 200)
assert(isinstance(response.data, list))


# Test Case 2
params2 = {
    'query': 'brc',
    'species': 'gorilla_gorilla',
    'limit': '20'
}

request2 = factory.get('/gene_suggest/', params2)
response2 = view(request2)

assert(response2.status_code == 200)
assert(isinstance(response2.data, list))


# Test Case 3
params3 = {
    'query': 'brc',
    'species': 'homo_sapiens'
}

request3 = factory.get('/gene_suggest/', params3)
response3 = view(request3)

assert(response3.status_code == 400)
assert(isinstance(response3.data, dict))


# Test Case 4
params4 = {
    'query': 'brc'
}

request4 = factory.get('/gene_suggest/', params4)
response4 = view(request4)

assert(response4.status_code == 400)
assert(isinstance(response4.data, dict))


# Test Case 5
params5 = {
    'query': 'brc',
    'species': 'chelonoidis_abingdonii',
    'limit': '20'
}

request5 = factory.get('/gene_suggest/', params5)
response5 = view(request5)

assert(response5.status_code == 200)
assert(isinstance(response5.data, list))
