

text_to_encode = 'bbbccaaaaadbb'

def encode(input):
    if input == None:
        return ""
    else:
        prevChar = ""
        counter = 1
        encode = ""
        for x in input:
            if x != prevChar:
                if prevChar != "":
                    encode += str(counter) + prevChar
                    counter = 1
            else:
                counter += 1
            prevChar = x
        encode += str(counter) + prevChar
        return encode

print(encode(text_to_encode))