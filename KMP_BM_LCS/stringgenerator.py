import random
import string
import sys

def generatestring(stringlength,charlist):
    st=[]
    i=k=0
    j=stringlength
    data_chars=set()
    while(i<j):
        ch=random.choice(list(charlist))
        data_chars.add(ch)
        k=random.randint(1,j)
        st+=[ch]*k
        j-=k
    return ["".join(st),data_chars]

def stringgenerator_call(maxlength):

    data_len=random.randint(1,maxlength)
    pattern_len=random.randint(1,data_len)

    stringchars=string.ascii_lowercase
    all_chars=set(stringchars)

    data,data_chars=generatestring(data_len,all_chars)
    diff_chars=all_chars-data_chars

    #choosing to sent the same chars or call chars or different chars
    selection_number=random.randint(1,3)
    selection_dict={1:all_chars,2:data_chars,3:diff_chars}

    pattern,pattern_chars=generatestring(pattern_len,selection_dict[selection_number])
    print()
    return [data,pattern]    






    
