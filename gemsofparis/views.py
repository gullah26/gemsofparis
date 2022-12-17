from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path
from django.shortcuts import render

""" 
Custom 404, 500, 403 and 400 page, 
which handles bad request, server error, http forbidden,
and page not found.
"""


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

def handler500(request):
    """ Error Handler 500 - server error """
    return HttpResponseServerError()
    return HttpResponse(status=500)
    raise Exception("server error")  
    raise HttpResponseServerError() 
    a_typo 
    return render(request, "errors/500.html", status=500)

def handler403(request, exception):
    """ Error Handler 403 - HTTP Forbidden """
    return render(request, "errors/403.html", status=403)

    def permission_denied_view(request):
        raise PermissionDenied


    urlpatterns = [
        path('403/', permission_denied_view),
    ]


def handler400(request, exception):
    """ Error Handler 400 - bad request """
    return render(request, "errors/400.html", status=400)

    