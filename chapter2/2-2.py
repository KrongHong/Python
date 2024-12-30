
print("=" * 50)
##문자열 포매팅
### 제일 간단한 포메팅
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}살 입니다.'
print(a)

### 제일 간단한 포메팅
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age * 2}살 입니다.'
print(a)

print("=" * 50)

## Count
a = 'hobby'
print(a.count("o")) # count() 문자열의 글자 개수 출력

print("=" * 50)

print(a.index("b")) # index() 문자열의 위치를 출력

print("=" * 50)

a = ", ".join('abcd') # join() 문자열을 하나씩 잘라서 그안에 ", " 이걸 삽입하겠다
print(a)
a = ", ".join(['a', 'b', 'c', 'd']) # join() 문자열을 하나씩 잘라서 그안에 ", " 이걸 삽입하겠다 -> list 형식도 가능
print(a)

print("=" * 50)
a = "Life is too short"
print(a.replace("Life", "Your leg")) # 문자열 대체하기


print("=" * 50)
a = "Life is too short"
print(a.split()) # split() => List의 형식으로 표시해준다 -> split()의 기본은 띄워쓰기를 기준으로 나누게 된다.


print("=" * 50)
a = "a:b:c:d"
print(a.split(":")) # split(":") => 띄워쓰기가 아닌 : 을 기준으로 나누고 싶다면 split(":")를 사용하면 된다