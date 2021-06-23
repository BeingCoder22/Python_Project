import sys
import os


def main():
    # Check and retrieve command line arguments
    if len(sys.argv) !=3:
        print(__doc__)
        sys.exit(1) #Return a non-zero vlaue to indicate abnormal termination
    
fileIn = sys.argv[1]
ExtID = sys.argv[2]

# Verify source file
if not os.path.isfile(fileIn):
    print("Error: {} does not exits".format(fileIn))
    sys.exit(1)

# Process the file
with open(fileIn, 'r') as fpIn, open('output.txt','w') as fpOut:
    lineNumber = 0
    for line in fpIn:
        lineNumber += 1
        line = line.rstrip() #strip trailing spaces and newline      
        fpOut.writelines("dn: uid={}, ou=People, o=Extranet, o=lmig.com\nchangetype: modify\nreplace: lmextusercustomer\nlmextusercustomer: {}\n\n".format(line, ExtID))
        # Need \n, which will be translated to platform-dependent newline
    print("Numbers of lines: {}\n".format(lineNumber))
fpOut.close()
if __name__=='__main__':
    main()


#dn: uid=priyaaja, ou=People, o=Extranet, o=lmig.com
#changetype: modify
#replace: lmextusercustomer
#lmextusercustomer: 1234567