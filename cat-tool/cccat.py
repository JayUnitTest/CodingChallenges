import argparse
import sys

def main():

    if len(sys.argv) != 2:
        print("insert a file name")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as fileObj:
            file_content = fileObj.readlines()
            print(file_content)
    except FileNotFoundError:
        print("File not found:", filename )
     
if __name__ == '__main__':
    main()


''' main purpose of sys.argv is to :
> it is a list of command line arguments
> len(sys.argv) provides the number of command-line arguments
> sys.argv[0] is the name of the current python script. 
 so in this case, we are checking if a total of 2 arguments are passed in the command-line - the script and the filename
'''
