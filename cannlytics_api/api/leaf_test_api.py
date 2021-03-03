from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.firebase import get_collection, get_document, update_document


@api_view(['GET'])
def lab_results(request, format=None):
    """Get lab results data."""

    # Query labs.
    if request.method == 'GET':
        limit = request.query_params.get("limit", 1000)
        order_by = request.query_params.get("order_by", "")
        # TODO: Get any filters from dict(request.query_params)
        labs = get_collection('tests/leaf/lab_results', order_by=order_by, limit=limit, filters=[])
        return Response({ "data": labs}, content_type="application/json")


@api_view(['GET'])
def mmes(request, format=None):
    """Get licensee (MME) data."""

    # Query labs.
    if request.method == 'GET':
        limit = request.query_params.get("limit", None)
        order_by = request.query_params.get("order_by", "")
        # TODO: Get any filters from dict(request.query_params)
        labs = get_collection('tests/leaf/mmes', order_by=order_by, limit=limit, filters=[])
        return Response({ "data": labs}, content_type="application/json")

