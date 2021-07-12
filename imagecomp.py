import os
import sys
from PIL import Image
from tkinter.filedialog import *


# define a function for
# compressing an image
def compressMe(file, verbose = False):
    
      # Get the path of the file
    filepath = os.path.join(os.getcwd(), 
                            file)
      
    # open the image
    picture = Image.open(filepath)
    
    save_path = asksaveasfilename()
      
    picture.save(save_path+file, 
                 "JPEG",
                 optimize = True, 
                 quality = 55)
    return
  
# Define a main function
def main():
    
    verbose = False
      
    # checks for verbose flag
    if (len(sys.argv)>1):
        
        if (sys.argv[1].lower()=="-v"):
            verbose = True
                      
    # finds current working dir
    cwd = os.getcwd()
  
    formats = ('.jpg', '.jpeg')
      
    # looping through all the files 
    # in a current directory
    for file in os.listdir(cwd):
        
        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, verbose)
  
    print("Done Compressing")
  
# Driver code
if __name__=='__main__':
    main()