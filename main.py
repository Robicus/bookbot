text_to_analyze = "frankenstein.txt"

with open(f"/home/ubuntu/workspace/github.com/Robicus/bookbot/books/{text_to_analyze}") as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return(len(words))

def count_characters(text):
    counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if not char in counts:
                counts[char] = 1
            else:
                counts[char] += 1
    return counts

def sort_on(dict):
    return dict["count"]

def sort_and_count(data):
    sorted_data = []
    for char in data:
        sorted_data.append({"letter": char, "count": data[char]})

    sorted_data.sort(reverse=True, key=sort_on)

    return sorted_data

def print_report():
    print(f"--- Begin report of books/{text_to_analyze} ---")
    print(f"{count_words(file_contents)} words found in the document \n")

    character_counts = count_characters(file_contents)
    sorted_data = sort_and_count(character_counts)

    for dict in sorted_data:
        # {'letter': 'e', 'count': 46043}
        print(f"The {dict['letter']} was found {dict['count']} times")

    print(f"\n--- End report ---")    

print_report()