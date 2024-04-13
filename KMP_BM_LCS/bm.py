def create_badmatch_table(pattern,pattern_len):
    badmatch_dict={}
    for i in range(pattern_len):
        badmatch_dict[pattern[i]]=pattern_len-i-1
    badmatch_dict['*']=pattern_len
    return badmatch_dict

def bmalgo(data,pattern,data_len,pattern_len):
    
    if(data_len>=pattern_len):
        badmatch_dict=create_badmatch_table(pattern,pattern_len)
        i=j=k=(pattern_len-1)
        while(i<data_len):
            if(data[i]==pattern[j]):
                    i-=1
                    j-=1
            else:
                if(data[i] not in badmatch_dict.keys()):
                    data_char="*"
                else:
                    data_char=data[i]
                i=k+badmatch_dict[data_char]
                if(k==i):
                    i=i+1
                k=i
                j=pattern_len-1
            if(j==-1):
                print("Index of match " +str(i+1) +" " +data[(i+1):(i+pattern_len+1)])
                return 1
        if(i>=data_len):
            print("No Match Found")
    else:
        print("Pattern Length is more than Data Length")
    return 0
