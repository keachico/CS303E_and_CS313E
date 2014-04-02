import string

def main():

    str1 = raw_input("Please enter a string: ")
    cipher(str1)

def cipher(str1):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    str1 = string.lower(str1) #change str1 to all lowercase letters
    new_string = ''

    for ch in str1:  #goes through every letter in str1
        
        if ch == ' ': #case when ch is a space
            new_string = new_string
            
        else:
            
            letter_index = string.find(alpha, ch) #index of ch in the alphabet
            
            if (letter_index == 25): # special case - 'z'
                new_letter = "a"
                new_string = new_string + new_letter

            elif (letter_index == -1): # special case - non-letters
                new_string = new_string
                
            else: 
                new_letter = alpha[(letter_index)+ 1 ] #change ch to next letter in alphabet
                new_string = new_string + new_letter
            
    print new_string
        
        
main()
