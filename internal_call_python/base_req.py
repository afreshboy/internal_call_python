class BaseReq:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


def dict2base_req(d):
    return BaseReq(d['num1'], d['num2'])


def base_req2dict(base_req):
    return {
        'num1': base_req.num1,
        'num2': base_req.num2
    }
