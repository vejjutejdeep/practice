def decode(string_decode):

    decoded_string = []

    return decoded_string

def code(list_encode):

    encode_string = ""

    for i in list_encode:

        encode_string = encode_string + i +  ":;"

    print(encode_string[:-2])

    return encode_string

def encode_decode(sentence):

    if type(sentence) == list:

        code(sentence)

    else:

        decode(sentence)
    
encode_decode(["lint", "code", "love", "you"])
encode_decode("lint:;code:;love:;you")