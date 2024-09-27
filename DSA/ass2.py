# from .model improt employee
# from .serilizer import emp_selrelizer
# from django import ResponseHTTP,


# class Emlployee(Model.viewset):

#     # @isauthicated
#     def Post(self,request):
#         username = request['username']
#         password = request['password']
#         employee = employee.object.filter(username = username & password = password, icontains = "v_name")
#         employee = emp_selrelizer(employee = employee)

#         return ResponseHTTP(employee) 

    
#     def setter(self):
#         name = self.name

#     def getter(self):
#         return self.name

# class Post(Emlployee.Model.Viewset):

#     sqlalchemy.

# def find_missing_number(lis):

#     max = 0
#     mis = -1
#     for i in lis:
#         if i > max:
#             max = i
#     for  i in range(0,max):
#         if i not in lis:
#             mis = i
#             break
#     if mis == -1:
#         max += 1
#         return max
#     return mis

# print(find_missing_number([3, 0, 1]))

arr = [1,5,4,3,2,4]
dic = {}
rep = 0
mis = 0
for i in arr:
    if i in dic:
        dic[i] += 1 
    else:
        dic[i] = 1
for i in range(1, len(arr) + 1):
    if i not in arr:
        mis = i
        break
for i in dic:
    if dic[i] > 1:
        rep = dic[i]
        break