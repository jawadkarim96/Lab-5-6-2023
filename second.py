import hashlib
import PyPDF2
import pathlib 

#task 1 comparing both hashes...
calculatedHash = "c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c"
filePath = open('Lab5-6-2023.pdf' ,'rb')
file = filePath.read()
hashOfFile = hashlib.sha256(file).hexdigest()
if calculatedHash == hashOfFile:
    print("Both hashes are same.")
else:
    print("Both hashes are not equal.")
#task number 2...
textFilePath = open('file.txt' , 'rb')
textFile = textFilePath.read()
hashOfTextFile = hashlib.sha256(textFile).hexdigest()
print("sha-256 hash of text file: " , hashOfTextFile)

#task number 3...
#message 1...
message1Path = open('message1.bin' , 'rb')
message1 = message1Path.read()
#MD-5 hash
hashOfMessage1 =hashlib.md5(message1)
print("MD-5 hash of message1 : " ,hashOfMessage1.hexdigest()) 
#sha-1 hash
secondHashOfMessage1 = hashlib.sha1(message1)
print("Sha-1 hash of message1 : " , secondHashOfMessage1.hexdigest())
#message 2...
message2Path = open('message2.bin' , 'rb')
message2 = message2Path.read()
#MD-5 hash
hashOfMessage2 =hashlib.md5(message2)
print("MD-5 hash of message2 : " ,hashOfMessage2.hexdigest()) 
#sha-1 hash
secondHashOfMessage2 = hashlib.sha1(message2)
print("Sha-1 hash of message2 : " , secondHashOfMessage2.hexdigest())
#results 
print("Result : There is collision of MD-5 function but different sha-1 hash function.")