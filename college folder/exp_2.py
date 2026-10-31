list1 = input("Enter elements of the first list separated by spaces: ").split() 
list2 = input("Enter elements of the second list separated by spaces: ").split() 
union_list = list(set(list1) | set(list2)) 
print("Union of the two lists:", union_list) 
