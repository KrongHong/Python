## 집합 : 자료형이다

## set() 
    ## 출력되는 순서는 랜덤으로 나오게 된다.
    ## 특별한 순서가 있는것이 아니므로 index로 접근하는 것이 불가능 Ex) s1[0]은 불가능
    ## 중복된 숫자는 제거되게 된다.
## 사용 이유
    # 교집합, 합집합, 차집합, 중복 제거
s1 = set([1,2,3]) # list자료형을 set이라는 집합으로 묶었음
s1 = {1,2,3}
print(s1)

s1 = set("Hello")
print(s1)

# set에서 뽑고 싶으면 list or tuple 로 만들고 뽑아야한다.
s1 = set([1,2,3])
li = list(s1)
print(li)
print(li[0])

print("-" * 50)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 구하기
print("교집합 : {} ".format(s1 & s2))
print("교집합 : {} ".format(s1.intersection(s2)))

print("-" * 50)

# 교집합 구하기
print("합집합 : {} ".format(s1 | s2))
print("합집합 : {} ".format(s1.union(s2)))

print("-" * 50)

# 차집합
print("합집합 : {} ".format(s1 - s2))
print("합집합 : {} ".format(s1.difference(s2)))

## 집합 내장 함수 : add, update, remove
    # add : 하나씩 추가할 때
s1 = set([1,2,3])
insert_value = 4
s1.add(insert_value)
print("집합에 {}라는 요소를 더하면 {}가 나온다.".format(insert_value, s1))

print("-" * 50)

    # update : 동시에 여러개를 추가할 때
s1 = set([1,2,3])
s1.update([4,5,6])
print("Update 결과 : {}".format(s1))

s1 = set([1,2,3])
s1.update([4,4,5,6])
print("Update 결과 : {}".format(s1))

print("-" * 50)

    # remove : 특정 값 제거하기
s1 = set([1,2,3])
s1.remove(2)
print("reomove 결과 : {}".format(s1))

