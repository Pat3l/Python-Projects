def anagram(word1 , word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    print("This program checks the validation of anagram.")
    word1 = input("Enter the first word: \n")
    word2 = input("Enter the second word: \n")
    print(anagram(word1 , word2))

#Will return True if word can be rearanged else false.