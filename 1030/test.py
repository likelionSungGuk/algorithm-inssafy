import re
p = re.compile('[a-z]+')
#1. match
m = p.match('python')
print(m)
#<re.Match object; span=(0, 6), match='python'>

n = p.match("3 python")
print(n)
#None - 3으로 시작하기 때문에 match되지 않음.

l = p.match("python 3")
print(l)
#<re.Match object; span=(0, 6), match='python'> - 3이 뒤에 있는거는 괜찮음

#2. search()
m = p.search("python")
print(m)

l = p.search("3 python")
print(l)

#3. find()
result = p.findall("life is too short 33 AA")
print(result)

#4. findall()
result = p.finditer("life is too short")
print(result)

for r in result:
    print(r)

#5. 컴파일 옵션
## 5-1. DOTALL
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

## 5-2. IGNORE

p = re.compile('[a-z]+', re.I)
m = p.match('python')
l = p.match('Python')
n = p.match('PYTHON')
print(m, l, n)

## 5-3. MULTILINE
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))