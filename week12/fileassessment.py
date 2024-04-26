fname="new"
file=open(f"C:/Users/ishan/OneDrive/Desktop/python/{fname}.txt","r")
data=file.readlines()
file.seek(0)
d1=file.read()
d2=d1.split(" ")
count=0
for d in d1 :
    count+=1
    
print(f"numbers of words in the file is :{len(d1)}/nNumber of lines in file is {len(data)}")
for letter in d1:
    if letter !=" ":
        count+=1
print(f"Number  of letter in the file is :{count}")
l="I"
l_count=0
for line in data:
    if line.startswith(l):
        l_count+=1
print(f"Number of line starting with letter{l} : {l_count}")
            
file.close()
