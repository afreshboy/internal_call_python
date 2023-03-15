from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import internal_call

from . import base_req
import json


@csrf_exempt
def get_count(request):
    if request.method == 'GET':
        num1 = request.GET.get("num1", "0")
        num2 = request.GET.get("num2", "0")
        return HttpResponse(int(num1) + int(num2))
    else:
        return HttpResponse("failed")


@csrf_exempt
def post_count(request):
    if request.method == 'POST':
        body = request.body
        req = json.loads(body, object_hook=base_req.dict2base_req)
        return HttpResponse(int(req.num1 + req.num2))
    else:
        return HttpResponse('invalid method: %s' % request.method)


@csrf_exempt
def internal_call(request):
    if request.method != 'GET':
        return HttpResponse('invalid method: %s' % request.method)
    service_id = request.headers.get('X-SERVICE-ID')
    method = request.headers.get('X-SERVICE-METHOD')
    uri = request.headers.get('X-SERVICE-URI')
    num1 = request.headers.get('X-SERVICE-VALUE1')
    num2 = request.headers.get('X-SERVICE-VALUE2')
    headers = {
        'TEST_HEADER': 'test_header'
    }
    if method == 'GET':
        param_map = {
            'num1': num1,
            'num2': num2
        }
        resp = internal_call.internal_call_get(service_id, uri, param_map, headers)
        return HttpResponse(resp)
    elif method == 'POST':
        req = base_req.BaseReq(num1, num2)
        resp = internal_call.internal_call_post(service_id, uri, req, headers)
        return HttpResponse(resp)


@csrf_exempt
def ping(request):
    pass
