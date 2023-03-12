# 덧셈을 통한 곱셈 프로그램
# 삼항연산자 및 함수 활용


def multifly(a, b):
    s = 0
    a_abs = a
    b_abs = b

    negatives = 0
    
    if a < 0 :                  # a 음수 판별
        negatives += 1          # 음수일 때, negative +1
        a_abs = -a              # 음수일 때, a의 절댓값을 a_abs로 반환

    if b < 0 :                  # b 음수 판별
        negatives += 1          # 음수일 때, negative +1
        b_abs = -b              # 음수일 때, b의 절댓값을 b_abs로 반환
    
    # positive: True
    # negative: False

    sign = negatives % 2 == 0   # negative가 짝수인 경우 True, 아닌 경우 False 반환 (둘 다 음수인 경우, negative 값이 2, True 반환)
    '''
    if negatives % 2 == 0 :
        sign = 1
    else :
        sign = 0
    '''


    for i in range (b_abs) :    # b의 절댓값 만큼 반복해서 a를 더함
        s = s + a_abs

    if (sign == False) :        # sign값이 0인 경우 (a, b 둘 중 하나만 음수인 경우)
        s = -s                  # 결과값에 -를 붙여서 음수로 반환 (a, b 둘 중 하나만 음수인 경우 곱은 음수)

    return s

a = -2
b = -3
c = multifly(a, b)
print(a, 'X', b, '=', c)