#A python program to illustrate how to decrypt a code using the cipher technique Casesar Cipher Technique
from pprint import pprint


def Caesar_Cipher(cipher_text, s):
    result=""


    #Transverse text
    for i in range(len(cipher_text)):

        #Assigning each character in the cipher_text to the variable char
        char = cipher_text[i]

        # Decrypt uppercase characters
        if (char.isupper()):

            #Cipher Caesar uses represents alphabets as numbers in order to perfrom the shift
            #Obtaining the numerical equivalent of the each letter in the cipher/ index of each character
            i_index = ord(char)- ord("A")

            #Since we are decryting the shifting will be done in the left direction
            #This is done to obtain the character's position in the Caesar Cipher algorithm
            char_postion_in_CC = (i_index - s) % 26 + ord("A")

            #convert to char_position_in_CC to string form
            char_string= chr(char_postion_in_CC)

            #assign value to result
            result += char_string

        
        # Decrypt lowercase characters
        elif (char.islower()):

             #Cipher Caesar uses represents alphabets as numbers in order to perfrom the shift
            #Obtaining the numerical equivalent of the each letter in the cipher/ index of each character
            i_index = ord(char)- ord("a")

            #Since we are decryting the shifting will be done in the left direction
            #This is done to obtain the character's position in the Caesar Cipher algorithm
            char_postion_in_CC = (i_index - s) % 26 + ord("a")

            #convert to char_position_in_CC to string form
            char_string= chr(char_postion_in_CC)

            #assign to result
            result += char_string

        #Digits(for digits, we want to shift them as they are)
        elif (char.isdigit()):
            #For, we want to shift its actual value
            char_string = (int(char) - s) % 10  #since they are digits

            #assign value to result
            result += str(char_string)

        #For punctuations and symbols
        #we want to leave them as they are if they are punctuations and symbols
        

        else:
            result += char

    #return reult        
    return result





#Creating a function to read from Ciphertext.txt file
def read_Ciphertext_from_txt(inputfileName, outputFileName, s = 7, decrypt=True):
    
    #Read from inputfile(ciphertext.txt)
    with open(inputfileName, "r", encoding="latin-1") as f_in:

        #Create outputfile and read from it
        with open(outputFileName, "w", encoding="latin-1") as f_out:

            # iterate over each character in input file
            for cipher_text in f_in:

                #encrypt/decrypt the cipher_text in ciphertext
                New_plain_text = Caesar_Cipher(cipher_text, s)

                #write the new line to output file
                f_out.write( New_plain_text)

   #Status message                 
    print("The file {} has been decrypted successfully and saved to {}".format(inputfileName, outputFileName))

#inputfilepath
inputFile =  "C:/Users/Mba/Documents/VS CODE/Python ML assignment/Ciphertext.txt"

#outputfilepath
outputFile = "C:/Users/Mba/Documents/VS CODE/Python ML assignment/Ciphertext_decrypted.txt"

read_Ciphertext_from_txt(inputFile, outputFile, s=7, decrypt = True)

#CONVERTING OUTPUTFILE INTO A PDF FILE

from fpdf import FPDF
  
# save FPDF() class into a
# variable pdf
pdf = FPDF(orientation='P', unit='mm', format='A4')
 
# Add a page
pdf.add_page()
 
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 12)

# open the text file in read mode
with open("C:/Users/Mba/Documents/VS CODE/Python ML assignment/Ciphertext_decrypted.txt", "r", encoding="latin-1") as f:

 
# create a cell

    for x in f:
        pdf.multi_cell(200, 10, txt = x, border=0,
                 align = 'L', fill=False)
        

 
# save the pdf with name .pdf
pdf.output("Ciphertext_decrypt.pdf")  


