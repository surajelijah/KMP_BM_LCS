Main File - Simulation.py

Execution - python Simulation.py [maxlength of strings] [testcases to observe]

NOTE: Both the parameters are necessary for execution.

Modules - bm.py  [ BM Algorithm ] 
	  kmp.py [ KMP Algorithm ]
	  lcs.py [ LCS Algorithm ] 
     	  stringgenerator.py [ Random string generator ] 

Generating random strings
  	
	[ NOTE: 1<= patternlength <= datalength <=10^4 ]
	
	Step 1-  Get a random number using the random module of python and assign it to data length such that 1<=datalength<=10^4
	Step 2 - Get a random number using the random module of python and assign it to pattern length such that 1<=patternlength<=datalength
	Step 3 - Choose a randome character(ch) form set of characters provided as argument(charlist).Append the character chosen to a set(s).
	Step 4 - Chose a random number j between 1 and maxlength
	Step 5 - Append the character(ch) to string(st) j times.Then decrement the maxlength by j and go to step 3 until the string length is maxlength

	Thus the random string is generated.
	[ NOTE: Data string is generated with all the characterlist
		Pattern string is generated using a random number(selection_number):1<=selection<=3
			1: same set of characters as the data string is used.
			2: all different characters are used from that in data string
			3: all the characters are used ]
Solution Logic:

	1.Based on the testcases and the maxlength provided in the arguments the simulation gets inititated.
	2.For each test cases a pair <pattern, data> is generated which has the maximum length provided in the argument.
	3.For each pair the <pattern,data> BM and KMP Algorithms are run.
	4.If both of them return 0 then LCS Algorithm is run on them.

	Thus is the execution of the program.
 	
