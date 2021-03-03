
from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .auth import authenticate
from utils.firebase import get_document, update_document


@api_view(['GET', 'POST'])
def users(request, format=None):
    """Get, update, or create users."""
    # try:
    #     claims = authenticate(request)
    # except:
    #     return Response({"error": "Could not authenticate."}, status=status.HTTP_400_BAD_REQUEST)

    # Get user(s).
    if request.method == 'GET':
        print("Getting user...")
        # limit = request.query_params.get("limit", None)
        # order_by = request.query_params.get("order_by", "state")
        # # TODO: Get any filters from dict(request.query_params)
        # labs = get_collection('labs', order_by=order_by, limit=limit, filters=[])
        user = {}
        return Response({ "data": user}, content_type="application/json")

    # Update or create user(s).
    elif request.method == 'POST':
        # TODO: Check if user already exists.
        # get_document
        print("Creating a user...")
        timestamp = datetime.now().isoformat()
        email = request.query_params.get("email", "")
        user = {
            "email": email,
            "created_at": timestamp,
            # "uid": user.uid,
            "photo_url": f"https://robohash.org/${email}?set=set5",
        }
        print(user)
        return Response({ "success": True}, content_type="application/json")