list1 = [1, 5, 7, 8, 9, 6, 4, 0, 48, 69, 45]
sort_type = input("Enter the type of sorting: \"asc or desc\": ")


def order_list(list1, sort_type):
    new_list = list1.copy()
    for i in range(len(new_list) - 1):
        for j in range(i + 1, len(new_list)):
            if sort_type == "asc":
                if new_list[i] > new_list[j]:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
            elif sort_type == "desc":
                if new_list[i] < new_list[j]:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
                else:
                    print("Invalid sorting type. Please enter 'asc' or 'desc'.")
                    return
    return new_list


sorted_list = order_list(list1, sort_type)
print(sorted_list)
