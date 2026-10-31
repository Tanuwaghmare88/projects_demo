def word_count(str): 
    counts = dict() 
    words = str.split() 
    for word in words: 
        if word in counts: 
            counts[word] += 1 
        else: 
            counts[word] = 1 
    return counts  # This line should be outside the for loop

print(word_count(input("Enter a string:\n")))
