def caesarEncrypt(text, shift):
    encrypted = ""
    for i in range(len(text)):
        # If when shifted greater than Z, go back to A
        if(ord(text[i])+int(shift)>90):
            encrypted = encrypted + chr(ord(text[i])+int(shift)-26)
        else:
            encrypted = encrypted + chr(ord(text[i])+int(shift))
            
    print(encrypted)
    return encrypted


def caesarDecrypt(text, shift):
    decrypted = ""
    for i in range(len(text)):
        # If when shifted less than A, go forward to Z
        if(ord(text[i])-int(shift)<65):
            decrypted = decrypted + chr(ord(text[i])-int(shift)+26)
        else:
            decrypted = decrypted + chr(ord(text[i])-int(shift))
            
    print(decrypted)
    return decrypted

###################
# ONLY MAIN BELOW #
###################

def main():
    text = input('Message: ').upper()
    opt = input('Choose 1 to encrypt or 2 to decrypt: ')
    shift = input('Shift pattern : ')

    if opt == '1':
        caesarEncrypt(text, shift)
    if opt == '2':
        caesarDecrypt(text,shift)

if __name__ == '__main__':
    main()
    