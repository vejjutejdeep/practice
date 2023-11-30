def convertToDecimal(number):

    convertednumber = ""

    while(number):

        convertednumber = convertednumber + str(number % 2)

        number = number // 2

    convertednumber = (convertednumber)[::-1]

    return convertednumber

print(convertToDecimal(128))
print(convertToDecimal(13))
print(convertToDecimal(16))