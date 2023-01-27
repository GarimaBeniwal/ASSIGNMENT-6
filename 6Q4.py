def pngrm(str):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char not in  str.lower():
            return False
        else:   
            return True


str1=(input("enter a string"))
if(pngrm(str1) == True):
    print("Yes, it is a panagram")
else:
    print("No, it isn't a panagram")