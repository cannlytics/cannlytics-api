from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "cannlytics_api"
urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.base, name="base"),
    path("v1/labs/", views.labs),
    path("v1/labs/<uuid:org_id>/", views.labs),
    path("v1/labs/<uuid:org_id>/analyses/", views.lab_analyses),
    path("v1/labs/<uuid:org_id>/logs/", views.lab_logs),
    # Optional: Find a way to generalize
    # path("v1/<slug:endpoint>/", views.get_labs, name="endpoint"),
    # TODO: Build out additional endpoints
    # /regulations
    # /instruments
    # /analytes
    # /instruments
    # /lab_results
]

# Adding optional format suffixes to our URLs
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
urlpatterns = format_suffix_patterns(urlpatterns)
