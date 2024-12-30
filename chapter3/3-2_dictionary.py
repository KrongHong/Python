## Dictionary는 Key와 Value로 이루어진 자료 like Hash, Map, Json, Object

## Dictionary의 경우는 API에 자주 활용이 된다.

## Dictationary : Key를 통해서 Value를 찾는다.

# Key는 무조건 하나만 있어야 한다. Like : Primary Key
dic = {'name' : 'key', 'phone' : '010-6628-9180', 'birth' : '1118'}
print(dic)

a = {'a' : [1,2,3]} # a라는 key에 list를 넣는다
print(a)

print("-" * 50)

# Dictionary에 새로운 값을 추가
a = {1 : 'a'}
a[2] = 'b' # 2라는 key, b라는 value
a[3] = [1,2,3] # 3라는 key, 리스트 value
print(a)


#Dictionary에 값을 삭제
dic = {'name' : 'key', 'phone' : '010-6628-9180', 'birth' : '1118'}
del dic['name']
print(dic)

#Dictionary에서 Key를 사용해 Value를 얻기
grade = {'Pey' : 10, 'Julliet' : 99}
print(grade['Pey'])

print("-" * 50)

# Dictaionary 관련 내장 함수

 #keys() : 현재 사용중인 Key를 모두 출력한다
 # 리스트보다 메모리를 덜 차지하는 dict_keys라는 자료를 만든다.
dic = {'name' : 'key', 'phone' : '010-6628-9180', 'birth' : '1118'}
print(dic.keys())

for k in dic.keys() :
    print(k)


 # values() : 현재 사용중인 Value를 모두 출력한다
print(list(dic.values()))


 # items() : Key와 Value를 쌍을 얻는다.
print(dic.items())

print("-" * 50)

 # clear() : Key, Value를 모두 지운다

 # get() : Key를 이용해서 Value의 값을 가져온다
 # get() 과 그냥 가져오는것에 대한 차이 : 오류문이 뜨느냐 None값이 나오느냐 차이
dic = {'name' : 'key', 'phone' : '010-6628-9180', 'birth' : '1118'}
# print(a['hi']) # Error
print(dic.get('hi')) # 없는 Key를 가져오기 때문에 "None"값 발생
print(dic['phone'])
print(dic.get('hi', "값이 없습니다. 다른 Key값을 찾아보세요"))
print(dic.get('phone', "값이 없습니다. 다른 Key값을 찾아보세요"))

print("-" * 50)

# key의 값이 있는지 확인
dic = {'name' : 'key', 'phone' : '010-6628-9180', 'birth' : '1118'}
print('name' in dic)
print('hi' in dic)

