dict = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 4]
}

print(sorted(dict.items(), key = lambda item: item[1][2], reverse = True))
# # 딕셔너리를 리스트로 변환
# list_dict = [x for x in dict.items()]
# print(list_dict)
# # 리스트를 정렬
# list_dict.sort(key=lambda x: x[1][2], reverse=True)
# print(list_dict)
# # 리스트를 딕셔너리로 다시 변환
# dict_sorted = {x[0]: x[1] for x in list_dict}

# print(dict_sorted)