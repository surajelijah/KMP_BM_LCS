import sys
import time
import bm as bmcode
import lcs as lcscode
import kmp as kmpcode
import stringgenerator as sgen

def calling_algorithms(data,pattern):
    data_len=len(data)
    pattern_len=len(pattern)

    print()
    print("Data : "+data +"("+str(data_len)+")")
    print()
    print("Pattern: " +pattern+"("+str(pattern_len)+")")
    print()

    print("Using [ BM Algorithm ]")
    st_time=time.time()
    algo1=bmcode.bmalgo(data,pattern,data_len,pattern_len)
    print("Time take for BM Algorithm(sec) : "+str(time.time()-st_time))
    print()

    print("Using [ KMP Algorithm ]")
    st_time=time.time()
    algo2=kmpcode.kmpalgo(data,pattern,data_len,pattern_len)
    print("Time take for KMP Algorithm(sec) : "+str(time.time()-st_time))
    print()

    if(algo1!=1 and algo2!=1):
        print("Printing [ LCS ] if no match found in BM and KMP")
        st_time=time.time()
        lcscode.lcsalgo(data,pattern,data_len,pattern_len)
        print("Time take for LSC Algorithm(sec) : "+str(time.time()-st_time))
    
if __name__== '__main__':

    if(len(sys.argv)!=3):
        print()
        print("Provide boththe arguments [maxlength of strings] [testcases to observe]")
    else:
        maxlength=int(sys.argv[1])
        testcases=int(sys.argv[2])
        for i in range(testcases):
            print('-----------------------------')
            data,pattern=sgen.stringgenerator_call(maxlength)
            calling_algorithms(data,pattern)

    


