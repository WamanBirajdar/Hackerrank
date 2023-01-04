# Your task is to wrap the string into a paragraph of width 4.
# text wrap on width 4
import textwrap

def wrap(string,width):
    return textwrap.fill(string,width)

if __name__=="__main__":
    string=input("Enter a  string ")
    width=int(input("Enter a width"))
    result=wrap(string,width)
    print(result)
    
    
'''
 Enter a  string ABCDEFGHIJKLIMNOQRSTUVWXYZ
Enter a width4
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
 '''
