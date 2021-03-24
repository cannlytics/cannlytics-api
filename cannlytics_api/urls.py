from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views
from .api import labs, users, leaf_test_api, cannlypedia

# Change URLs to not end in a trailing slash.
# https://stackoverflow.com/questions/46163838/how-can-i-make-a-trailing-slash-optional-on-a-django-rest-framework-simplerouter
router = routers.SimpleRouter(trailing_slash=False)

app_name = "cannlytics_api"
urlpatterns = [

    # Base endpoints
    path("", views.index, name="index"),
    path("v1/", views.base, name="base"),

    # Lab endpoints
    path("v1/labs/", labs.labs),
    path("v1/labs/<uuid:org_id>/", labs.lab),
    path("v1/labs/<uuid:org_id>/analyses/", labs.lab_analyses),
    path("v1/labs/<uuid:org_id>/logs/", labs.lab_logs),

    # Leaf test endpoints
    path("test/leaf/mmes/", leaf_test_api.mmes),
    path("test/leaf/lab_results/", leaf_test_api.lab_results),
    # path("/test/leaf/users"),
    # path("/test/leaf/areas"),
    # path("/test/leaf/areas/update"),
    # path("/test/leaf/strains"),

    # TODO: Better handle 404's

    # User endpoints
    # path("v1/users/", users.users),
    # path("v1/users/<uuid:org_id>/", users.users),

    # TODO: Build out additional endpoints

    # /regulations

    # /instruments

    # /analytes

    # /instruments

    # /lab_results

    # Optional: Find a way to generalize
    # path("v1/<slug:endpoint>/", views.get_labs, name="endpoint"),

    # Functional
    path('scholars/', cannlypedia.scholars),
]

# Adding optional format suffixes to our URLs
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
urlpatterns = format_suffix_patterns(urlpatterns)
