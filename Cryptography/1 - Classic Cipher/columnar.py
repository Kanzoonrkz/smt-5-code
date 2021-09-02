import math

def columnarEncrypt(text, key):
    encrypted = ""

    # Create and fill array with "_"
    rows, cols = (len(key), math.ceil(len(text)/len(key)))
    arr = [["_" for i in range(rows)] for j in range(cols)]

    # Structure:
    # cols   rows -->          arr[cols][rows]
    #  |
    #  |
    #  v

    # Fill the actual character to array
    for i in range(cols):
        for j in range(rows):
            try:
                arr[i][j] = text[j+(i*(rows))]
            except IndexError:
                pass
    
    # Create list representing string:key as list of ascii
    keyList = []
    for i in range(len(key)):
        keyList.append(ord(key[i]))

    # Convert ascii to sorted number for future exporting
    for i in range(len(key)):
        keyList[keyList.index(min(j for j in keyList if j>(i-1)))] = i

    # Add character to encrypted, per column based on keylist
    for j in range(rows):
        for i in range(cols):
            try:
                encrypted = encrypted + arr[i][keyList.index(j)]
            except IndexError:
                pass
    
    print(encrypted)
    return(encrypted)

def columnarDecrypt(text, key):
    decrypted = ""

    # Create and fill array with null value
    rows, cols = (len(key), math.ceil(len(text)/len(key)))
    arr = [["" for i in range(rows)] for j in range(cols)]

    # Create list representing string:key as list of ascii
    keyList = []
    for i in range(len(key)):
        keyList.append(ord(key[i]))

    # Convert ascii to sorted number for future exporting
    for i in range(len(key)):
        keyList[keyList.index(min(j for j in keyList if j>(i-1)))] = i

    # Add character to array based on key
    for j in range(rows):
        for i in range(cols):
            try:
                arr[i][keyList.index(j)] = text[i+(j*(cols))]
            except IndexError:
                pass

    # Add character to decrypted
    for i in range(cols):
        for j in range(rows):
            decrypted = decrypted + arr[i][j]
    
    print(decrypted)
    return(decrypted)


###################
# ONLY MAIN BELOW #
###################

def main():
    text = input('Message: ').upper()
    opt = input('Choose 1 to encrypt or 2 to decrypt: ')
    key = input('Keyword : ').upper()

    if opt == '1':
        columnarEncrypt(text, key)
    if opt == '2':
        columnarDecrypt(text, key)
        


if __name__ == '__main__':
    main()
    