from firebase_admin import auth


def authenticate(request):
    """Identify the user's Firebase account using an ID token."""
    authorization = request.headers['Authorization']
    token = authorization.split(' ')[1]
    claims = auth.verify_id_token(token)
    uid = claims['uid']
    request.session['uid'] = uid  # Save user's custom claims in a session?
    return claims
