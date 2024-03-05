import time

print("Palindrome Checker!")
time.sleep(2)

word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
	print(f"The word ({word}) is a Palindrome.")
else:
	print(f"The word ({word}) is not a Palindrome.")
