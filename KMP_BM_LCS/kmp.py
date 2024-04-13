def create_prefix_array(pattern,pattern_len):
    prefix_array=[0]*pattern_len
    i=1
    j=0
    prefix_array[0]=0
    while(i<pattern_len):
        if(pattern[i]==pattern[j]):
            j+=1
            prefix_array[i]=j
            i+=1
        else:
            if(j!=0):
                j=prefix_array[j-1]
            else:
                prefix_array[i]=0
                i+=1
    return prefix_array


def kmpalgo(data,pattern,data_len,pattern_len):
    if(data_len>=pattern_len):
        prefix_array=create_prefix_array(pattern,pattern_len)
        i=j=0
        while(i<data_len):
            if(data[i]==pattern[j]):
                if(j==pattern_len-1):
                    print("Index of match " +str(i-j) +" " +data[(i-j):i+1])
                    return 1
                else:
                    i+=1
                    j+=1
            elif (j>0):
                j=prefix_array[j-1]
            else:
                    i+=1
        if(i>=data_len):
             print("No Match Found")
    else:
        print("Pattern Length is more than Data Length")
    return 0
