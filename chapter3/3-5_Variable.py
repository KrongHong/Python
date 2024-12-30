
# a의 주소값이 나오게 된다. 주소를 바라본다고 생각하면 편하다
a = [1,2,3]
b = a

print(id(a))
print(id(b))

print(a is b)

print("-" * 50)

# a와 b가 같은 메모리 주소를 바라보고 있기 때문에 같은 값이 나오게 된다.
a = [1,2,3]
b = a
a[1] = 4
print(id(a))
print(id(b))
print(a is b)
print(a)
print(b)

print("-" * 50)

# a를 변경해도 b가 변경되지 않게 하기 위해서 슬라이싱을 이용 => 슬라이싱을 통해서 다른 메모리 주소가 만들어지게 된다.
a = [1,2,3]
b = a[:] # 슬라이싱을 통해서 a의 처음부터 끝까지 슬라이싱해서 b로 가져온다
a[1] = 4
print(a)
print(b)

print("-" * 50)

from copy import copy
a = [1,2,3]
b = copy(a)
# b = a.copy() # 이것도 가능
a[1] = 4
print("copy() 함수를 이용한 복사")
print(a)
print(b)

print("-" * 50)

## 다양한 변수 만들기 방법
tup = a, b = ('python', 'life')
print(type(tup))
print(a)
print(type(a))
print(b)

print("-" * 50)

## **스왑** 하는 부분 굉장히 편리함
a = 3
b = 5
print("스왑하기 전 :")
print(a)
print(b)

print("스왑하고 난 후 : ")
a, b = b, a
print(a)
print(b)