def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
    word_count = count_words(book)
    character_count = count_characters(book)
    list_of_entries = to_list(character_count)
    list_of_entries.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{word_count} words found in the document\n\n")
    for entry in list_of_entries:
        for key, value in entry.items():
            print(f"The '{key}' character was found {value} times\n")
    print("--- End report ---")



def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_characters(text):
    characters = {}
    lower_string = text.lower()
    for char in lower_string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
  for char in dict:
      return dict[char]

def to_list(dict):
    list_of_dicts = []
    for entry in dict:
        if entry.isalpha():
            list_of_dicts.append({entry: dict[entry]})
    return list_of_dicts

main()
