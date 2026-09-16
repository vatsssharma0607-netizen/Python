def count_letters(text):
    uppercount = 0
    lowercount = 0
    for char in text:
        if char.isupper():
            uppercount += 1
        elif char.islower():
            lowercount += 1
    print("Original String: ", text)
    print("No. of Uppercase characters: ", uppercount)
    print("No. of Lowercase characters: ", lowercount)
count_letters("My name is Vatss Sharma")
