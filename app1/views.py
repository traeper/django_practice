from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import service
# Create your views here.


def api_do_job(request):

    service.do_job()

    # write algorithm here.
    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'job process terminated successfully'

    return JsonResponse(response_data)
