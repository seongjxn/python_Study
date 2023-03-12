# float, if-else 활용


height = float(input("키를 입력하세요.      (단위는 m 입니다.) : "))
weight = float(input("몸무게를 입력하세요. (단위는 kg 입니다.) : "))

bmi = weight / height ** 2

if bmi < 18.5 :
    print("저체중")
elif bmi < 23 :
    print ("정상")
elif bmi < 25 :
    print("과체중")
elif bmi < 30 :
    print("비만 1단계")
elif bmi < 40 :
    print("비만 2단계")
else :
    print("심각한 비만 상태")

print("비만도 = {:2f}" . format(bmi))