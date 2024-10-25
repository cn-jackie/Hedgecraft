def getMinTotalDistance(dist_centers):
    dist_centers.sort()
    n = len(dist_centers)
    min_distance = float('inf')

    # 计算前缀和
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + dist_centers[i]

    # 计算总距离的辅助函数
    def total_distance(l, r):
        return (dist_centers[r] * (r - l + 1) - (prefix_sum[r + 1] - prefix_sum[l]))

    # 遍历第一个仓库可能的位置
    for i in range(n):
        for j in range(i, n):
            # 计算所有配送中心到最近仓库的总距离
            total_distance_i = total_distance(0, i)
            total_distance_j = total_distance(j, n - 1)
            total_distance_between = total_distance(i + 1, j - 1) if i + 1 <= j - 1 else 0
            total_distance = total_distance_i + total_distance_j + total_distance_between
            min_distance = min(min_distance, total_distance)
    
    return min_distance

# 测试函数，计算给定配送中心位置列表的最小总距离
result = getMinTotalDistance([1, 2, 5, 6])
print(result)
