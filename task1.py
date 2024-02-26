"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

orig_list = [1, 3, 5, 3, 5, "tru", "tru", "test", 3]
result_list = []

for item in orig_list:
    if item not in result_list:
        if orig_list.count(item) > 1:
            result_list.append(item)

print(result_list)
