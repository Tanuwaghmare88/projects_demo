def demo():
    lst1 = input("Enter the list of words separated by spaces: ").split()
    target_word = input("Enter the word to remove: ")
    i = int(input("Enter the occurrence number to remove (1-based index): "))

    count = 0
    for idx, word in enumerate(lst1):
        if word == target_word:
            count += 1
            if count == i:
                lst1.pop(idx)
                break

    print("Updated list:", lst1)

demo()
