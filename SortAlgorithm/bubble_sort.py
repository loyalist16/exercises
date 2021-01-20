# 冒泡排序

def bubble(array):
    sort_index = len(array) - 1
    for i in range(len(array) - 1, 0, -1):
        # 判断是否有序, 如果当前遍历已无发生改变, 这说明当前排序已然有序, 不需在执行下去
        is_sorted = True
        # 遍历到最后一次交换的位置, 代表其之后已经为有序
        if sort_index < i:
            i = sort_index
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                # 元素有交换, 所以标记为false
                is_sorted = False
                # 记录最后一次交换位置
                sort_index = j

        if is_sorted:
            break
    return array


if __name__ == '__main__':
    a = [3, 4, 2, 1, 5, 6, 7, 8]
    a = bubble(a)
    print(a)
