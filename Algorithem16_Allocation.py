def check(P, weights, k):
    """ 最大積載量 P で k 台のトラックに荷物を積めるか判定 """
    truck_count = 1
    current_weight = 0

    for w in weights:
        if current_weight + w > P:
            truck_count += 1  # 新しいトラックを使う
            current_weight = w
        else:
            current_weight += w
        
        if truck_count > k:
            return False  # トラックの数を超えたら NG

    return True  # すべての荷物を積めるなら OK

def find_minimum_P(n, k, weights):
    left, right = max(weights), sum(weights)  # P の最小値と最大値
    while left < right:
        mid = (left + right) // 2
        if check(mid, weights, k):
            right = mid  # より小さい P を試す
        else:
            left = mid + 1  # P が小さすぎて無理なら増やす
    return left

# 入力
n, k = map(int, input().split())
weights = [int(input()) for _ in range(n)]

# 出力
print(find_minimum_P(n, k, weights))
