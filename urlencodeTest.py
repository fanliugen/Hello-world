import urllib.parse
import requests

data={
    'name':'测试',
    'age':30,
    'sex':'male'
}
queries = urllib.parse.urlencode(data)

print(queries)

unurl = urllib.parse.unquote(queries)
print(unurl)






