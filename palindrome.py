#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 15
count = 0
with open("words.txt") as file:
  for word in file:
    word = word.strip()
    if word == word[::-1]:
      count +=1
      print(count)
