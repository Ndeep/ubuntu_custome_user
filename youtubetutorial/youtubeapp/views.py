from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from youtubeapp.models import Question
from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

# CACHE_TTL=getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)


@api_view(['GET'])
def view_books(request):
    question=Question.objects.all()
    results=[ques.to_json() for ques in question]
    return Response(results,status=status.HTTP_201_CREATED)

def log_request(sender, environ, **kwargs):
    method = environ['REQUEST_METHOD']
    host = environ['HTTP_HOST']
    path = environ['PATH_INFO']
    query = environ['QUERY_STRING']
    query = '?' + query if query else ''
    print('New Request -> {method} {host}{path}{query}'.format(
        method=method,
        host=host,
        path=path,
        query=query,
    ))


