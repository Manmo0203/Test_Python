#print output to terminal
print("Hello World")

#data type
v1 = 1
v2 = 2.56
v3 = "String"
print(type(v1))
print(type(v2))
print(type(v3))

#max integer for division
print(11//6)
#remainder for division
print(11%6)
#power of...2 to the power of 5
print(2**5)

#data type conversion
print(int(v2))
print(type(int(v2)))
print(float(v1))
print(type(float(v1)))

#string default function
s1 = "test string space"
print(len(s1))
print(s1[3])        #start from position 0
print(s1[4:8])
print(s1[:8])
print(s1[6:])
print(s1[2:15:4])   #from position 2 to 15, interval for each 4 character

s2 = "Hello"
s3="123"
print(s2.isupper())
print(s2.islower())
print(s2.upper().isupper())
print(s2.lower().islower())
print(s2.isnumeric())
print(s3.isnumeric())
print(s2.replace("l","p",2))