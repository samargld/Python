class A:
    def __init__(self,lst,i=0):
        self.lst=lst
        self.i=i
        self.res=self.pop()
    def __str__(self) :
        return str(self.res)
    def pop(self):
        if not self.i:
            v=self.lst[len(self.lst)-1]
            lst = self.lst[0:len(self.lst)-1]
            return lst,v
        else :
            v = self.lst[self.i]
            lst=self.lst[0:self.i]+self.lst[self.i+1:]
            return lst,v
lst=[]
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    lst.append(item)
print(lst)
b=int(input("which index you want to remove?"))
c=A (lst,b)
print(c)
