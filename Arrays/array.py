def create_string(dict):
    print(dict.keys())
    str = ''
    for i in dict.keys():
        if 'name' in i:
            if 'my name is' in str:
                str += ' ' + dict[i]
            else:
                str += "my name is %s" % dict[i]

            


        if 'designation' in i:

            str += " my designation is %s" % dict[i]
    
    return str


dic = {"firstname": "john", "lastname": "kens", "middlename": "Rose", "designation": "developer"}
print(create_string(dic))