fp = open("text.txt", "r") #"r" (to read) is by default, so not really needed
print(fp.read()) #print the entire content of the file
fp.close() #good practice to close the file

#same exact thing with context manager
with open("text.txt", "r") as f:
    print(f.read())

# lets read from the the same file, line by line
print("read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp: #we iterate over the file line by line
        print(f'{line_number}: {line}', end="") #ask print not to add a new line with the end = ""
        #print(line.rstrip())
        line_number +=1
print("done printing")
