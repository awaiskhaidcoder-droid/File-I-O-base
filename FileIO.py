# for writing
f=open("Awais.txt","w")
f.write("I am trying to learn python with my best struggling")
f.close()
# for reading 
file=open("Awais.txt","r")
data=file.readline()
print(data)
f.close()
# for append data
f=open("Awais.txt","a")
f.write(" and I will try my best ")
f.close()
# for reading  and append operation
f=open("Awais.txt","a+")
data=f.readline()
print(data)
f.write(" Please pray for me")


