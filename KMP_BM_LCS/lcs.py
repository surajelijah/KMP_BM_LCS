def print_LCS(memoised_lcs_table,data,pattern,data_len,pattern_len):
    lcs_array=[]
    i=data_len
    j=pattern_len
    while(i>0 and j>0):
        if(data[i-1]==pattern[j-1]):
            lcs_array.append(data[i-1])
            i-=1
            j-=1
        elif(memoised_lcs_table[i-1][j]>memoised_lcs_table[i][j-1]):
            i-=1
        else:
            j-=1
    return "".join(lcs_array[::-1])

def lcsalgo(data,pattern,data_len,pattern_len):
    memoised_lcs_table=[[0]*(pattern_len+1)]*(data_len+1)
    for i in range(data_len+1):
        for j in range(pattern_len+1):
            if(i==0 or j==0):
                memoised_lcs_table[i][j]=0
            elif(data[i-1]==pattern[j-1]):
                memoised_lcs_table[i][j]=1+memoised_lcs_table[i-1][j-1]
            else:
                memoised_lcs_table[i][j]=max(memoised_lcs_table[i-1][j],memoised_lcs_table[i][j-1])
    lcs=print_LCS(memoised_lcs_table,data,pattern,data_len,pattern_len)
    if(len(lcs)!=0):
        print("LCS between them is " + lcs)
    else:
        print("No LCS between them")
    return
