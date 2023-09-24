

#Lengthy Method
#Check whether a character is vowel or consonant
char = str(input("Enter the character: "))
Vowels = ["A","E","I","O","U","a","e","i","o","u"]
Consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
if len(char) == 1:
    if char in Vowels:
        print("The given character is vowel.")
    if char in Consonants:
        print("The given character is consonant.")
else:
    print("Enter single character.")
    
#Also need to specify this
# if char == int:
#     print("Enter string.")
