def outinorder(*args):
    '''
    简单的冒泡排序算法，由小到大
    :param args: 应该输入3个数字，以逗号隔开
    :return:
    '''
    # lst = list(args)
    # lst.sort()
    lst = list(args)
    lg = list(range(len(lst)))
    for i in range(len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                lg[j], lg[j+1] = lg[j+1], lg[j]
    print(lg)
    return lst
print(outinorder(951,521,2,8,4))