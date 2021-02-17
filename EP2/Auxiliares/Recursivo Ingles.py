key = [2,0,1]
matrix = [["0","1", "1"], ["0","1", "1"], ["1","1", "2"], ["2","0", "1"], ["2","2", "0"]]


def QuickSort (matrix, key, start = 0, end = None):

    if end is None:
        end = len(matrix)-1
    if start < end:
        p = partition(matrix, start, end, key)
        QuickSort(matrix, key, start, p - 1)
        QuickSort(matrix, key, p + 1, end)

    return matrix


def partition (matrix, start, end, ordekeym):

    pivot = matrix[end]
    i = start

    for j in range (start, end):

        if matrix[j][key[0]] < pivot[key[0]]:
            matrix[j], matrix[i] = matrix[i], matrix[j]
            i = i + 1

        if matrix[j][key[0]] == pivot[key[0]] and len(key) == 2:
            if matrix[j][key[1]] < pivot[key[1]]:
                i = i+1

        if matrix[j][key[0]] == pivot[key[0]] and len(key) == 3:
            if matrix[j][key[1]] < pivot[key[1]]:
                i = i + 1
            if matrix[j][key[1]] == pivot[key[1]]:
                if matrix[j][key[2]] < pivot[key[2]]:
                    i = i + 1
                if matrix[j][key[2]] == pivot[key[2]]:
                    break

    matrix[i], matrix[end], = matrix[end], matrix[i]
    return i

print(QuickSort(matrix, key))
