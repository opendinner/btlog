def bubblesort(data):
    """
    冒泡排序算法
    :param data: 待排序的列表
    :return: 排序后的列表
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            print(f"比较 {data[j]} 和 {data[j+1]}，当前列表状态：{data}")
            # 如果当前元素大于下一个元素，则交换它们的位置
            if data[j] > data[j+1]:
                # 交换位置
                data[j], data[j+1] = data[j+1], data[j]
                print(f"交换 {data[j]} 和 {data[j+1]}，当前列表状态：{data}")

        print(f"第 {i+1} 次冒泡后，当前列表状态：{data}\n")
    return data

if __name__ == '__main__':
    data = [23, 45, 12, 67, 34, 89, 10, 5]
    print("原始列表：", data)
    sorted_data = bubblesort(data)
    print("排序后的列表：", sorted_data)