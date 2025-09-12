from sortedcontainers import SortedDict

# 使用第三方库 sortedcontainers
tree_map = SortedDict()
tree_map[3] = "Third"
tree_map[1] = "First"
tree_map[2] = "Second"

# 输出按键排序: (1, 'First'), (2, 'Second'), (3, 'Third')
for key, value in tree_map.items():
    print(f"{key}={value}")