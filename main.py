from stats import text_to_string, count_words, count_characters, sort_high_to_low

path = "books/frankenstein.txt"
str = text_to_string(path)
count = count_words(str)
chars = count_characters(str)
sorted = sort_high_to_low(chars)



print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")
for item in sorted:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")