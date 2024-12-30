# 파일의 객체를 만드는 방법
# f = open("chapter5/새파일.txt", 'w', encoding="UTF-8")
# for i in range(1,11) :
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close

# f = open("chapter5/새파일.txt", 'r', encoding="UTF-8")
# for i in range(1,11) :
#     line = f.readline()
#     print(line)
# f.close

# print("-" * 50)

# f = open("chapter5/새파일.txt", 'r', encoding="UTF-8")
# while True :
#     line = f.readline()
#     if not line : break
#     print(line)
# f.close

# print("-" * 50)

# while True :
#     data = input()
#     if not data :
#         break
#     print(data)

# print("-" * 50)

# f = open("chapter5/새파일.txt", 'r', encoding="UTF-8")
# while True :
#     line = f.readlines()
#     if not line : break
#     print(line)
# f.close

# 메모장 줄바꿈 현상 없애기
f = open("chapter5/새파일.txt", 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines :
    line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거한다.
    line = line.replace('\n', '') # replace를 이용해서 줄 바꿈 문자를 제거
    print(line)
f.close

# 'a'를 통해서 업데이트 하기
f = open("chapter5/새파일.txt", 'a', encoding="UTF-8")
for i in range(11,21) :
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

