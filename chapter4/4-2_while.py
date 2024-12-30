# treeHit = 0
# while treeHit < 10 :
#     treeHit += 1
#     print("나무를 {}번 찍었습니다.".format(treeHit))
#     if treeHit == 10 :
#         print("나무가 넘어갑니다")


# print("-" * 50)

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# """

# number = 0
# while number != 4 :
#     print(prompt)
#     number = int(input()) # input자체는 무조건 String으로 처리하게 된다. 그러서 String이라는 변수를 int형을 타입을 변경해줘야 종료가 된다.

# print("-" * 50)

# coffee = 10
# money = 300
# while money : 
#     print("돈을 받았으니 커피를 줍니다")
#     coffee -= 1
#     money -= 100
#     print("남은 커피의 양은 %d 입니다. 현재 남은 돈의 양은 %d원 입니다." %(coffee,money))
#     if coffee == 0:
#         print("커피가 다 떨어 졌습니다. 판매를 중지합니다.")
#         break
#     elif money == 0:
#         print("돈이 다 떨어 졌습니다.")
#         break
    

# coffee = 10
# while True :
#     money = int(input("돈을 넣어 주세요 : "))
#     if money >= 300 :
#         print("커피를 줍니다.")
#         coffee -= 1
#         print("거스름돈은 %d원 입니다." %(money-300))
#     else :
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 양의 커피는 %d 입니다." %coffee)
#     if coffee == 0 :
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다")
#         break


# a = 0
# while a < 10 :
#     a += 1
#     if a % 2 == 0 : 
#         continue
#     print(a) # 홀수만 출력


# test_list = ['one', 'two', 'three']
# for i in test_list :
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a :
#     print(first + last)


# marks = [90, 25, 67, 45, 80] # 학생들의 시험 점수 리스트

# number = 0 # 학생에게 붙여 줄 번호
# # for mark in marks :
# #     number += 1
# #     if mark >= 60 :
# #         print("%d번 학생은 합격입니다." %number)
# #     else :
# #         print("%d번 학생은 불합격입니다." %number)

# for mark in marks :
#     number += 1
#     if mark < 60 :
#         continue
#     print("%d번 학생 축하하빈다. 합격입니다." %number)

## Range() 함수
# a = range (1, 101)
# print(a)

# add = 0
# for i in range(1,11) :
#     add += i
#     print(add)

for i in range (1, 10) :
    for j in range (1, 10) : 
        print("%d x %d = %2d" %(i, j, i*j), end = "    ") # end는 한줄씩 출력되는걸 방지하고 한칸씩 띄워쓰기로 출력
    print(" ")
        