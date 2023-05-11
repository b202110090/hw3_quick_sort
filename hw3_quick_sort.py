# 先建立function供後續使用，以遞迴方式進行快速排序
def quick_sorting(number_list):
    # 顯示目前遞迴處裡的list
    print('目前處理的list:', number_list)
    # 如果子數列只剩一個數或沒有數，該子數列就離開遞迴
    if len(number_list) <= 1:
        print('達到目前子數列遞迴的終點\n')
        return number_list
    # 最左邊的元素作為標的
    pivot = number_list[0]
    # 小於pivot的數放到小區的子數列中
    small_than_pivot = []
    # 等於pivot的數放到此子數列中
    equal_to_pivot = []
    # 大於pivot的數放到大區的子數列中
    larger_than_pivot = []
    # 對number_list的元素逐一檢視，看是小於、大於或等於pivot，並將該元素放入子數列中
    for a in number_list:
        if a < pivot:
            small_than_pivot.append(a)
        elif a > pivot:
            larger_than_pivot.append(a)
        else:
            equal_to_pivot.append(a)

    # 顯示目前遞迴的pivot與大於小於pivot的有誰
    print('目前pivot的值：', pivot)
    print('目前與pivot一樣大的數列：', equal_to_pivot)
    print('目前比pivot小的數列：', small_than_pivot)
    print('目前比pivot大的數列：', larger_than_pivot)
    print('往下一步處理\n')
    # 投過遞迴，將子數列分別比完大小，脫離遞迴以後將各子數列按照小到大的順序組裝起來。
    return quick_sorting(small_than_pivot) + equal_to_pivot + quick_sorting(larger_than_pivot)

# 使用者輸入數列
input_number = input('請輸入整數列，數字之間以空白或逗號分隔，輸入完後按enter將進行排序：\n')
# 將字串的逗點處切開成字串陣列
number_list = input_number.split(",")
# 處理字串陣列空白當作分隔符號的狀況
number_list = " ".join(number_list).split()
# 將字串陣列轉為int陣列
number_list = [int(i) for i in number_list]

# 顯示排序前的數列
print('快速排序前的數列：\n', number_list)
# 進行快速排序
quick_sort_list = quick_sorting(number_list)
print('全部子數列的遞迴處理完畢\n')
# 顯示排序後的數列
print('快速排序後的數列：', quick_sort_list)
