a = True
print(a)
print(type(a))

print("-" * 50)

a = [1,2,3,4]
while a: # a는 값이 있으니깐 True로 반환되게 된다. pop을 이용해서 없어지면 False를 반환
    print(a)
    a.pop()


if [1234] : # list의 값이 들어잇으면 참 없으면 거짓
    print("참")
else : 
    print("거짓")

print("-" * 50)

a = bool([1,2,3])
print(a)

a = bool([])
print(a)