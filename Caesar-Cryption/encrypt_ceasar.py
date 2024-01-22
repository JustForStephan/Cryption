crypted = input("Enter the crypted text to break: ").upper()
crypted = [*crypted]
all_encryptions = []
all_encryptions_string = []
# encrypt all
for i in range(26):
    
    temp_text = []
    for letter in crypted:
        print(i)
        if ord(letter)+i > 90:
            temp_text.append(chr(ord(letter)+ i - 26))
        else:
            temp_text.append(chr(ord(letter)+i))       
    
    all_encryptions.append(temp_text)

# convert to readable string
for x in all_encryptions:
    temp_string = ""
    for y in x:
        temp_string = temp_string + y
    all_encryptions_string.append(temp_string)

# print all possibilities
print("\n The code has been broken. There are all possibilities:")
for x in all_encryptions_string:
    print(x)
print("Chose the one, which makes the most sense ;)")

    
