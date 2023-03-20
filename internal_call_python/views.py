from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .internal_call import *
from .base_req import *
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
        body = request.body.decode('utf-8')
        req = json.loads(body, object_hook=dict2base_req)
        return HttpResponse(int(req.num1) + int(req.num2))
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
        try:
            response = HttpResponse(internal_call_get(service_id, uri, param_map, headers))
            return response
        except:
            response = HttpResponse("error")
            response.status_code = 500
            return response
    elif method == 'POST':
        try:
            req = BaseReq(num1, num2)
            body = json.dumps(req, default=base_req2dict)
            response = HttpResponse(internal_call_post(service_id, uri, body, headers))
            return response
        except:
            response = HttpResponse("error")
            response.status_code = 500
            return response
    response = HttpResponse("invalid method: %s" % method)
    response.status_code = 403
    return response


@csrf_exempt
def ping(request):
    return HttpResponse("success")
