list1 = input("Enter the first list of elements separated by spaces: ").split() 
list2 = input("Enter the second list of elements separated by spaces: ").split() 
intersection_list = [] 
for item in list1: 
 if item in list2 and item not in intersection_list: 
  intersection_list.append(item) 
print("Intersection of the two lists:", intersection_list) 
