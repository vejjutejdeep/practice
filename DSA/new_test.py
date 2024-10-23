dic = {"tata": 'altroz', 'maruti': "ignis", 'nissan' : 'micra', "renault": "dustur"}
dic1 = dic
dic1['tata'] = 'nano'
# print(dic)

def check_palindrom(s):
    if s[::-1] == s:
        return True
    return False

def substring(s):
    max = ''
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            # print(s[i:j])
            if check_palindrom(s[i:j]):
                if len(s[i:j]) > len(max):
                    max = s[i:j]
    return max

s = "babad"
print(substring(s))
s = "cbbd"
print(substring(s))
s = "bb"
print(substring(s))