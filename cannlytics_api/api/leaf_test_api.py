# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from utils.firebase import get_collection, get_document, update_document
from utils.firebase import get_collection


@api_view(['GET', 'POST'])
def lab_results(request, format=None):
    '''Get lab results data.'''

    if request.method == 'GET':
        limit = request.query_params.get('limit', 1000)
        if limit:
            limit = int(limit)
        order_by = request.query_params.get('order_by', '')
        # TODO: Get any filters from dict(request.query_params)
        docs = get_collection(
            'tests/leaf/lab_results', order_by=order_by, limit=limit, filters=[]
        )
        return Response(docs, content_type='application/json')

    if request.method == 'POST':
        print('TODO: Create lab results')
        return NotImplementedError


@api_view(['GET'])
def mmes(request, format=None):
    '''Get licensee (MME) data.'''

    if request.method == 'GET':
        limit = request.query_params.get('limit', None)
        if limit:
            limit = int(limit)
        order_by = request.query_params.get('order_by', '')
        # TODO: Get any filters from dict(request.query_params)
        # e.g. {'key': 'name', 'operation': '==', 'value': 'xyz'}
        docs = get_collection(
            'tests/leaf/mmes', order_by=order_by, limit=limit, filters=[]
        )
        return Response(docs, content_type='application/json')
