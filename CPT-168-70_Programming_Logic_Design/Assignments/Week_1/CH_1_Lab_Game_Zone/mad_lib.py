'''
This program is for a Mad Lib game you can play in the terminal.
'''

# Mab lib reference
'''
"Hickory Dickory 'first_noun'
The mouse ran up the 'second_noun'.
The 'second_noun' struck 'third_number',
The mouse said 'fourth_noun',
Hickory Dickory 'first_noun'."
'''

first_noun = input("Enter a noun: ")
second_noun = input("Enter a noun that rhymes with the first noun: ")
third_number = input("Enter a number: ")
fourth_noun = input("Enter a noun that rhymes wih the number: ")

mad_lib = f'''
Example:
Hickory Dickory {first_noun}
The mouse ran up the {second_noun}.
The {second_noun} struck {third_number},
The mouse said {fourth_noun},
Hickory Dickory {first_noun}.
'''

print(mad_lib)