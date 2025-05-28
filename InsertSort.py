def insertsort(data):
    """
    插入排序算法
    :param data: 待排序的列表
    :return: 排序后的列表
    """
    for i in range(1, len(data)):
        key = data[i]#比较的元素key
        j = i - 1#key的前一个元素

        #如果key比前一个元素小，则将前一个元素向后移动一位，直到找到一个比key大的元素或者j为-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        #最后将key放到合适的位置
        data[j + 1] = key
        print(f"插入 {key} 到位置 {j + 1}，当前列表状态：{data}")
    
    return data

if __name__ == '__main__':
    data = [5, 3, 2, 4, 1, 6, 7, 8, 9, 10]
    insertsort(data)