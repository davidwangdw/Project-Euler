max = 20*19*18*17*16*15*14*13*12*11

i = 20

while i<max:
	if i%20 ==0 and i%19 ==0 and i%18==0 and i%17==0 and i%16==0 and i%15==0 and i%14==0 and i%13==0 and i%12==0 and i%11==0:
		print(i)
		break
	i += 1
