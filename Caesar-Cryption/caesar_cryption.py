while True:
    uncrypted = input("Enter the text to crypt: ").upper()
    if uncrypted == "EXIT()":
        break
    uncrypted = [*uncrypted]
    key = int(input("Enter the key for cryption: "))
    crypted = []
    for letter in uncrypted:
        if ord(letter)+key > 90:
            crypted.append(chr(ord(letter)+ key - 26))
        else:
            crypted.append(chr(ord(letter)+key))       
    print(crypted)
