#Filterd even num list 
Input_list = range(1,11)
out = []
for num in Input_list:
    if num %2 == 0:
        out.append(num)
print(out)



#filter even values from list
lis = [1,2,3,4,5,6,7,8,9,10,11,12]
lis2 =[i for i in lis if i%2 ==0]
print(lis2)
