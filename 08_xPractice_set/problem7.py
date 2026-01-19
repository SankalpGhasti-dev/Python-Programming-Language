
def rem(l, word):
    n = []
    for item in l:
        if (item != word):
            n.append(item.strip(word))
    return n 

l = {"Sankalp", "Rohan", "Soham", "an"}

print(rem(l, "an"))

# In this code, we have to remove an word also strip that word from other words in the list. so we have created a new list n and then we are checking if the item is not equal to the word to be removed, then we are stripping that word from the item and appending it to the new list. Finally, we are returning the new list.
