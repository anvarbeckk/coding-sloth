def checkTitle(s):
    words = s.split() # split the string into words
    for word in words: # check each word
        if not word.istitle(): # if the word is not title-cased
            return False # return false
    return True # if the all words are title-cased, it returns true


print(checkTitle("A Mind Boggling Achievement")) # -> True
print(checkTitle("A Simple C++ Program!")) # -> True
print(checkTitle("Water is transparent")) # -> False
