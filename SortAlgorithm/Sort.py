# 정렬 알고리즘


# ----------- bubbleSort -----------

def _bubbleSort(data) :
    for i in range(len(data)) :
        for j in range(0, len(data) -i -1) :
            if data[j] > data[j + 1] :
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

def bubbleSort(data) :
    if len(data) < 2 :
        return data
    else :
        return _bubbleSort(data)


# ----------- insertSort -----------

def _insertSort(data) :
    for i in range(1, len(data)) :
        for j in range(i, 0, -1) :
            if data[j - 1] > data[j] :
                data[j - 1], data[j] = data[j], data[j - 1]

    return data

def insertSort(data) :
    if len(data) < 2 :
        return data
    else :
        return _insertSort(data)


# ----------- quickSort -----------

def _quickSort(data) :
    for i in range(len(data)) :
        for j in range(0, len(data) -i -1) :
            if data[j] > data[j + 1] :
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

def quickSort(data) :
    if len(data) < 2 :
        return data
    else :
        return _quickSort(data)


# ----------- mergeSort -----------

def _mergeSort(data) :
    for i in range(len(data)) :
        for j in range(0, len(data) -i -1) :
            if data[j] > data[j + 1] :
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

def mergeSort(data) :
    if len(data) < 2 :
        return data
    else :
        return _mergeSort(data)


# ----------- selectionSort -----------

def _selectionSort(data) :
    for i in range(len(data) - 1) :
        min = i
        for j in range(i + 1, len(data)) :
            if data[j] < data[min] :
                min = j
        data[i], data[min] = data[min], data[i]

    return data

def selectionSort(data) :
    if len(data) < 2 :
        return data
    else :
        return _selectionSort(data)