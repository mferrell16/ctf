import itertools
import string
import zlib

keyspace = string.digits + string.ascii_lowercase
Correct = zlib.crc32(b'the_intended_answer')
print(Correct)
#Try all of character 
# (or `itertools.product(keyspace, repeat=5)`)
i = 1
while True: 
	print("Testing combinations of length", i)
	for combination in itertools.product(*[keyspace] * i):  
	    p = ''.join(combination)
	    starter = "Black Cybersecurity Association"
	    s = starter+p
	    #print("Trying: ", s)
	    testTry = zlib.crc32(s.encode("utf-8"))
	    if testTry == Correct:
	    	print("Answer found: ", s)
	    	with open('solved.txt', 'w') as f:
    				f.write('answer found: '+s)
	    	exit()
	print("Not found for length", i)
	i = i +1 


