#第一題
print("第一題")
def calculate(min, max):
    result=0
    for a in range(min,max+1):
        result+=a
    print(result)
calculate(1, 3) #1+2+3=6
calculate(4, 8) #4+5+6+7+8=30

#第二題
print("第二題")
def avg(data):
    total=0
    membernumber=data["count"]
    for a in range(membernumber):
        salary=data["employees"][a]["salary"]
        total+=salary
        average=total//membernumber
    print("員工為",membernumber,"位")
    print("total:",total,"元",end=",")
    print("average:",average,"元")
avg({
"count":3,
"employees":
    [
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) #

#第三題
print("第三題")
def maxProduct(nums):
    maxnumberlist=[]

    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            result=nums[i]*nums[j]
            maxnumberlist.append(result)
#             print("%d*%d=%2d"%(nums[i],nums[j],result))
    print(max(maxnumberlist))
#     nums.sort()
#     result=nums[-1]*nums[-2]
#     print(result)
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

#第四題
print("第四題")
def twoSum(nums, target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            result=nums[i]+nums[j]
            if result==target:
                #print(nums[i],nums[j])
#                 print(nums.index(nums[i]),nums.index(nums[j]))
                # return "數字"+str(target)+"為:nums["+str(nums.index(nums[i]))+"]+num["+str(nums.index(nums[j]))+"]"
                return "數字"+str(target)+"為:nums["+str(nums.index(nums[i]))+"]:"+str(nums[i])+" + num["+str(nums.index(nums[j]))+"]:"+str(nums[j])

            #print(result)
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#第五題
print("第五題")
def maxZeros(nums):
    n=0
    recordlist=[]
    for i in nums:
        #print("i",i)
        if i==0:
            n+=1
            recordlist.append(n)
        else:
            n=0
            recordlist.append(n)

    #print("n",n)
    return print(max(recordlist))

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0