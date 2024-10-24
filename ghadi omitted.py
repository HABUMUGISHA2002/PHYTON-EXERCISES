word=input("enter any word")
vawels="aiuoeAIUOE"
my_list=[]
for char in word :
    if char not in vawels :
        my_list.append(char)
myword="".join(my_list)
print(myword)