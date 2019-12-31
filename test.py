def add1():
    a = 23
    b = 34
    c= a+b
    return a, b, c

def ainb():
    a = {'code': 200, 'msg': '', 'data': {'orgname': '航天云网科技发展有限责任公司', 'homephone': '0311-4258713', 'phone': '15000000000', 'connect': '刘小红'}}
    b = {'code': 200, 'msg': '', 'data': {'orgname': '航天云网科技发展有限责任公司', 'homephone': '0311-4258713', 'phone': '15000000000', 'connect': '刘小红'}}
    if str(a) in str(b):
        print('in')
    else:
        print('not in')

print(ainb())
