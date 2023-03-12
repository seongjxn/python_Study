import random as r

# 순차 리스트 생성 (리스트, 생성할 리스트 크기)
def genList(L, size) :
    for i in range(size) :
        L.append(i)
    
    return L


# 랜덤한 리스트 생성 (리스트, 생성할 리스트 크기)
def genRandList(L, size) :
    L = genList(L, size)
    r.shuffle(L)

    return L


# 리스트 섞기 (리스트)
def shuffleList(L) :
    r.shuffle(L)

    return L


# 리스트 중 랜덤 추출 (리스트, 추출할 리스트 크기)
def pickList(L, size) :
    result = []

    for i in range(size) :
        pick = r.choice(L) 
        result.append(pick)
        L.remove(pick)
    
    return result


