# def tempratureFlu(temprature):

#     answer = []

#     for i in range(len(temprature) - 2):

#         count = 0

#         for j in range(i,len(temprature)):
            
#             if temprature[i] < temprature[j]:

#                 break
#             else:

#                 count += 1
        
#         answer.append(count)
        
#     if temprature[-2] < temprature[-1]:

#         answer.append(1)
    
#     else:

#         answer.append(0)
    
#     answer.append(0)
             
#     return answer

def dailyTemperatures(temperatures):
    ans=[0]*len(temperatures)
    stack=[]

    for i , t in enumerate(temperatures):
        print(list(enumerate(temperatures)))
        print(stack)
        while stack and t > stack[-1][0]:
            tempt ,tempi= stack.pop()
            ans[tempi] = i - tempi
        stack.append([t,i])
    return ans   

# temperatures = [73,74,75,71,69,72,76,73]
# print(temperatures)
# print(dailyTemperatures(temperatures))

# temperatures = [30,40,50,60]
# print(dailyTemperatures(temperatures))

# temperatures = [30,60,90]
# print(dailyTemperatures(temperatures))

temperatures = [55,38,53,81,61,93,97,32,43,78, 55]
print(dailyTemperatures(temperatures))