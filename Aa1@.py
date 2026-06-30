character = input("Enter a character: ")
if character.isupper():
    print(character, "is an uppercase letter")
elif character.islower():
    print(character, "is a lowercase letter")
elif character.isdigit():
    print(character, "is a digit")
else:
    print(character, "is a special character")
