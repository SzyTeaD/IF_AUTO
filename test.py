import json

a = {
 "code": "200",
 "msg": "",
 "data": "true"
}
c = str(a)
print(type(c))
b = json.loads(c)
print(type(b))