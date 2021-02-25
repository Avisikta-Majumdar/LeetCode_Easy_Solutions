result=int(a,2)+int(b,2) #Converting Binary no to decimal and adding this to no
r=str(bin(result)) #converting result to binary and then converting it to string format
return r[2:] # This will remove 0b part and will return remaining part
