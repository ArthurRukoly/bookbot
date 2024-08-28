def main():
    file_destination = "books/frankenstein.txt"
    file_contents = get_content(file_destination)
    words = get_number_of_words(file_contents)
    letters = get_number_of_letters(file_contents)
    print(f"--- Begin report of ${file_destination} ---")
    print(f"{words} words found in the document")
    for char in letters:
        print(f"The'{char}' character was found {letters[char]} times")
    print("--- End if Report --- ")
def get_content(file):
    with open(file) as f:
        return f.read()
    
def get_number_of_words(content):
    return len(content.split())

def get_number_of_letters(content):
    letter_dict = {}
    for char in content:
        char = char.lower()
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict
main()
