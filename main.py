from stats import get_book_text , count_words , char_count , sort_stuff , print_fancy_footer , print_fancy_header , print_indented , print_section_title
import sys
def main():             #define main here
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]                #Make it so I can change the file path later, because Boots INSISTED....
    book = get_book_text(file_path)              #call the get_book_text function here and assign it to a newly created var, passes the previously created file_path var to the function
    #print(f"{book}")                #print the var with the book text to the console
    count = count_words(book)               #call the count_words function here and assign it to the var, passing the result from book
    #print(count)               #print the counted words after the function finishes
    characters = char_count(book)
    sorted = sort_stuff(characters)
    report = ""
    report += "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {file_path}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {count} total words\n"
    # ... more lines ...
    #print(report)  # Print the entire report at once
    print_fancy_header("BOOKBOT")
    print_indented(f"Analyzing book found at {file_path}")
    print_section_title("Word Count")
    print(f"Found {count} total words")
    print_section_title("Character Count")
    # For aligning columns
    for char_dict in sorted:
        character = char_dict["char"]
        count = char_dict["count"]
        print(f"{character}: {count}")  # Left-align char, right-align count with width 7
    print_fancy_footer()



main()              #make the magic happen