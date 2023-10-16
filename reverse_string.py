# Input: Ask the user to enter a string and store it in the variable 'b'
b = input("Enter a string: ")

# Initialize an empty string 'd' to store the reversed string
d = ""

# Iterate through each character in the input string 'b'
for character in b :
    # Reverse the string by adding each character to the beginning of the 'd' string
    d = character + d

# Output: Display the reversed string
print("The string reversed is:",d)
