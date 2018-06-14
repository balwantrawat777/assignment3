#Question 1
a= input("enter any number ")
l=[]
l.append(a)
print(l)
#end

#Question 2
m=['google','facebook','apple','microsoft','tesla']
k=l+m
print(k)
#end


#Question 3
l=['red','orange','red','yellow','red']
print(l.count('yellow'))
#end

#Question 4
l=[2,4,5,1,7]
l.sort()
print(l)
#end


#Question 5
a=[1,2,3,4]
b=[3,4,5,6,7]
c=a+b
c.sort()
print(c)
#end


#question 6
a=[3,4,6,7]
a.pop()
a.append(9)
print(a)
#end



#Optional question
a=[0,1,2,3,4,5]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
#end