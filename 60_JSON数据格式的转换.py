import json
data = [{"name":"罗", "age": 1}, {"name":"玉", "age": 2}, {"name":"华", "age": 3}]

json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

d = {"name": "周杰伦", "addr":"台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

s = '[{"name": "罗", "age": 1}, {"name": "玉", "age": 2}, {"name": "华", "age": 3}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name": "周杰伦", "addr": "台北"}'
d = json.loads(s)
print(type(d))
print(d)