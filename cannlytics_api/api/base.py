from rest_framework.decorators import api_view
from rest_framework.response import Response

BASE = "https://api.cannlytics.com"
ENDPOINTS = ["labs"]
VERSION = "v1"


@api_view(["GET"])
def index(request, format=None):
    """Informational base endpoint."""
    message = "Welcome to the Cannlytics API."
    message += f"The current version is {VERSION} and is located at {BASE}/{VERSION}."
    return Response({"data": message}, content_type="application/json")


@api_view(["GET"])
def base(request, format=None):
    """Informational version endpoint."""
    message = f"Welcome to {VERSION} of the Cannlytics API."
    message += "Available endpoints:\n\n"
    for endpoint in ENDPOINTS:
        message += f"{endpoint}\n"
    return Response({"data": message}, content_type="application/json")
