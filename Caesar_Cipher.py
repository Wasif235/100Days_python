          
def cipher(original_text,shift_amount,encode_or_decode):
      output=""
      if encode_or_decode=='decode':
               shift_amount*= -1
      else:         
         for letters in original_text:
            if letters in original_text:
               output+= letters
            else:

               shifted_position= alphabet.index(letters)+ shift_amount
               shifted_position%=len(alphabet)
               output += alphabet[shifted_position]
            #return new_crypted_text
         print(f"here is the {encode_or_decode}d result:{output}\n")
should_continue= True      
while should_continue:
   alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   #direction= input("Type 'encode' to encrypt, type deode 'decode' to decrypt:\n").lower()
   text= input("type your message:\n").lower()
   shift=int(input("Type the shift number:\n"))
   direction= input("Type 'encode' to encrypt, type deode 'decode' to decrypt:\n").lower()
   cipher(text,shift,direction)    
   restart= input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n")
   if restart=='no':
       should_continue=False
       print("Goodbye")