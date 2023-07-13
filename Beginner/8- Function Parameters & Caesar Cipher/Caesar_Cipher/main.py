import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = art.logo

def caesar(text,shift,direction):
  end_text =""
  len_text = len(text)-1
  n = 0
  while(len_text>=0):
    if text[len_text] in alphabet:
        if text[len_text] == alphabet[n]:
            if direction == "encode":
                end_text = end_text + alphabet[n+shift]
            elif direction == "decode":
                end_text = end_text + alphabet[n-shift]
            len_text -= 1
            n = 0
        else:
             n+=1
    else:
        end_text += text[len_text]
        len_text-=1
  end_text = end_text[::-1]        
  print(f"Here's the {direction}d result: {end_text}")
  
print(logo)
End_Game = False

while not End_Game: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    try_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

if try_again == "yes":
    End_Game = False

else:
    End_Game = True

  