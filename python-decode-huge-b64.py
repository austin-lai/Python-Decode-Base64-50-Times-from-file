import sys,os,base64

msg=''
count = 0

## Get the full file path
## Reading the file as read only
filepath=os.path.join(sys.path[0], 'b64.txt')
with open(filepath,'r') as f:

    ## Read the file content with splitlines, to remove newlines, otherwise will broke the decode process below
    msg=f.read()

f.close()

for _ in range(50):
    msg = base64.b64decode(msg)
print(msg.decode('utf8'))




