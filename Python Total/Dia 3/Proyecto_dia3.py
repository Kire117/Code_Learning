user_text = input("Write any text: ")

letters = []

user_text = user_text.lower()

letters.append(input("Write the 1st letter of your choice: ").lower())
letters.append(input("Write the 2nd letter of your choice: ").lower())
letters.append(input("Write the 3rd letter of your choice: ").lower())

# print(letters_list)
print("\n LETTERS-------------------")
print(f"There are {user_text.count(letters[0])} {letters[0]}'s")
print(f"There are {user_text.count(letters[1])} {letters[1]}'s")
print(f"There are {user_text.count(letters[2])} {letters[2]}'s")

print("\n WORDS----------------")
words = user_text.split()

print(f"Words in text: {len(words)}")

print("\n FIRST AND LAST LETTER ----------")
print(f"First letter is {user_text[0]} and last letter is {user_text[-1]}")

print("\n REVERSED TEXT-----------------")
words.reverse()
reverse_text = " ".join(words)
print(f"reversed text: {reverse_text}")

print("\n WORD IN TEXT?-------------")
search_word = "Python" in user_text
dic = {True: 'is', False: 'is not'}

print(f"The word 'Python {dic[search_word]} on the text")



