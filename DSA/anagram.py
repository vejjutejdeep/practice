def is_anagram(com1, com2):


    if len(com1) == len(com2):

        dic = {}

        com1 = com1.lower()

        com2 = com2.lower()

        for i in range(len(com1)):

            if com1[i] in dic.keys():

                dic[com1[i]] += 1
            
            else:

                dic[com1[i]] = 1

            if com2[i] in dic.keys():

                dic[com2[i]] += 1
            
            else:

                dic[com2[i]] = 1
        
        # print(dic.values())        
        val = list(dic.values())

        # print(dic)

        # print(val)

        for i in range(len(val)):

            if val[i] % 2 != 0 :

                return False
        
        return True

    return False

s = "anagram"
t = "nagaram"
bool = is_anagram(s,t)
print(f"the anagram of {s} is {t} are {bool}\n")


s = "mace"
t = "race"
bool = is_anagram(s,t)
print(f"the anagram of {s} is {t} are {bool}\n")

s = "rat"
t = "tar"
bool = is_anagram(s,t)
print(f"the anagram of {s} is {t} are {bool}\n")

s = "car"
t = "bars"
bool = is_anagram(s,t)
print(f"the anagram of {s} is {t} are {bool}\n")

s = "mice"
t = "eicm"
bool = is_anagram(s,t)
print(f"the anagram of {s} is {t} are {bool}\n")

s = "cat"
t = "tac"
bool = is_anagram(s,t)
print(f"the anagram of {s} is {t} are {bool}\n")

