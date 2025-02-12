count = 0  # 比較回数をカウントする変数

def merge(A, left, mid, right):
    global count
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid] + [float('inf')]
    R = A[mid:right] + [float('inf')]
    i = j = 0

    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

# 入力の処理
n = int(input())
S = list(map(int, input().split()))

# マージソートの実行
mergeSort(S, 0, n)

# 結果の出力
print(" ".join(map(str, S)))
print(count)
