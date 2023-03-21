word=input(">: ")
rev_word= word[:0:-1]
print(rev_word)
if(word==rev_word):
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
