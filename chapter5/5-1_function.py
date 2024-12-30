# parameter : 함수에서 정의되어 사용되는 변수
# 인수 : 함수를 호출할 때 건네주는 변수

# def add(a, b) :
#     result = a + b
#     return result

def say() :
    return "Hi"

def add(a, b) : 
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))    

a = add(1,2) # add에는 return 값이 없다 그러므로
# 함수가 호출 되서 출력문이 나오고 a에 실제로 들어가는 값은 None값이 된다.
print(a)

print("-" * 50)

def sub(a, b) :
    return a - b

result = sub(a = 7, b = 3) # 매개변수 a, b를 직접 지정해주는 방식이다.
print(result)
result = sub(b = 3, a = 7) 
print(result)


print("-" * 50)

# 매개변수를 한번에 여러개를 받기위함 *args
def add_many(*args) :
    result = 0
    for i in args :
        result += i # *arg에 입력받은 모든 값을 더한다
    return result

print(add_many(1,2,3,4,5,6,7,8,9))


print("-" * 50)

# 매개변수 여러개를 갖는것과 한개를 갖는것을 섞어서 사용
def add_mul(choice, *args) :
    if choice == "add" : # 매개변수 choice에 "add"를 입력받았을 때
        result = 0
        for i in args : 
            result += i
    elif choice == "mul" : #매개변수 choice에 "mul"을 입력받았을 때
        result = 1
        for i in args : 
            result *= i
    return result

result = add_mul("add", 1,2,3)
print(result)

result = add_mul("mul", 1,2,3,4)
print(result)

print("-" * 50)

# Keyword를 통해서 매개변수 받기
# ** : Key, Value의 형태로 받겠다
def print_kwargs(**kwargs) :
    print(kwargs['a'])
    print(kwargs['b'])
    print(kwargs['name'])

print_kwargs(a=1, b=2, name = "Hong")

print("-" * 50)

# return값은 언제나 하나이다
def add_and_mul(a,b) :
    return a+b, a*b

a ,b = add_and_mul(3,4)
print(a)
print(b)
print(add_and_mul(3,4)) # 두개의 값이 따로 나오는것 X
# 두개의 값이 하나의 튜플료 묶여서 나오는 것이다.

print("-" * 50)

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man = True) :
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d 입니다." %old)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

say_myself("Hong", 26, True)
say_myself("Hong", 26) # 이미 함수에서 True라고 정의가 되어 있기 때문에 안써주더라도 똑같은 결과
say_myself("Hong", 26, False)


print("-" * 50)

# 지역 변수는 함수 내부에서만 사용되는 변수이다 밖에까지는 적용되지 않는다.
a = 1 # 전역 변수
def vartest(a) :
    a = a + 1 #매개변수 a와 a + 1의 a는 같은 a, But 결과의 a는 다른 a다

vartest(a)
print(a)

# 지역 변수를 함수 밖에서도 이용하는 법 : return 사용, 외부에도 변수 사용
a = 1 
def vartest(a) :
    a = a + 1 
    return a

a = vartest(a)
print(a)

a = 1 
def vartest() :
    global a
    a = a + 1 

vartest()
print(a)


print("-" * 50)

