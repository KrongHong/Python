e = [1,2, 'Life', 'is', ['Life', 'is']] # 파이썬은 리스트안에 자료형이 어떤게 들어가도 상관없음
print(type(e))

print("=" * 50)

a = [1, 2, 3]
print(a[0])
print(a[1] + a[2])

a = [1,2,3, ['a', 'b', 'c']] # 중요
print(a[3])
print(a[3][1])

print("=" * 50)

## 슬라이싱
a = [1,2,3,4,5]
print(a[0:5:2])

a = [1,2,3,['a', 'b', 'c'],4,5]
print(a[2:5])

print("=" * 50)

## 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)

print("=" * 50)

## 리스트의 길이 구하기
a = [1,2,3]
print(len(a))

print("=" * 50)

## 리시트의 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

del a[2] # 리스트의 값을 삭제한다
print(a)

a = [1, 2, 3, 4, 5]
del a[1::2]
print(a)

print('=' * 50)

## 리스트 관련 함수
 # 리스트에 값 추가하기 append, insert, expend
a = [1,2,3]
a.append(4)
print(a)

a = [1,2,3]
a.append(['a','b'])
print(a)

a = [1,2,3]
a.extend(['a','b'])
print(a)

a = [1,2,3]
a.insert(0,4) # 0번쨰 순서에 4라는 값 대입
print(a)

print('=' * 50)

 # 리시트의 값을 정렬 sort()
a = [1, 4, 3, 2]
a.sort() # 오름차순 정렬
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
a.reverse() # 그냥 거꾸로만 해줌
# sort() 후에 reverse()를 해야 내림차순으로 된다
print(a)


 # 리스트값을 삭제하는 함수
a = [1,2,3,1,2,3]
a.remove(3) #가장 먼저 나온 숫자 3을 삭제
print(a)

 # 리스트 요소에서 pop시키는 함수
a = [1,2,3]
print(a.pop()) # 마지막 요소를 pop
print(a)