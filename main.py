# Required Modules
import string 
import random

# Optional if statement
if __name__ == "__main__":
    while True: #Optional while loop
        s1 = string.ascii_lowercase #the string module funtion that gives us all the lower case letters
        s2 = string.ascii_uppercase # the string module funtion that gives us the uppercase letters
        s3 = string.digits # the string module function that gives us all the digits
        s4 = string.punctuation # the function of string module that returns punctuations (to make the password strong)

        plen = int(input("Password Length: ")) #input 

        # making the password by mixing the funtions we stored in the variables before 
        s = [] #the password empty list
        s.extend(list(s1)) #extending all the function outputs in the list
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        # packing the password
        final = "".join(random.sample(s, plen))

        #returning the output
        print(f"Your Password: {final}")
        
