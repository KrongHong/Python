money = 2000
card = True

if money >= 3000 and card : 
    print("택시타고 가소")
else :
    print("걸어 가소")


if not card : 
    print("택시타고 가소")
else :
    print("걸어 가소")


print("-" * 50)

print(1 in [1,2,3]) # list안에 1이 있니?
print(1 not in [1,2,3])


print("-" * 50)

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print("택시를 타고가라")
else :
    print("걸어가라")

print("-" * 50)

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket :
    print("택시를 타고가라")
elif 'money' not in pocket and card :
    print("택시를 타고가라")
else :
    print("걸어가라")

print("-" * 50)

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket :
    print("택시를 타고가라")
else :
    if card : 
        print("택시를 타고가라")
    else :
        print("걸어가라")