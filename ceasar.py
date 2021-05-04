def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        ch = text[i]
        if (ch.isupper()):
            result += chr((ord(ch) + s-65)% 26+65)
        else:
            result += chr((ord(ch) + s-97) % 26+97)
          
    return result
          
text = encrypt('phqgh', 3)
print(text)