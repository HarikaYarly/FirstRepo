'''python program to create a list by concatenating a given list which range goes from 1 to n
  sample list:['p','q'] n=5
  Sample Output:['p1','q1','p2','q2','p3','q3','p4','q4','p5','q5']'''
  
l = ['p','q']
n=5
ol=[]
for i in range(1,n+1):
    for j in l:
        #ol.append(j+str(i)) both the syntax can be used.
        ol.append('{}{}'.format(j,i))
print("Output list is : ",ol)
       