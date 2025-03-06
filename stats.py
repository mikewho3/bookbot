def get_book_text(path):                #define get_book_text here, gets the file path passed to it, because again, Boots INSISTED....
    try:                #Boots insisted I needed to add a try block in case the file is missing or not accessable...
        with open(path)as f:                #open the file, as f
            book = f.read()             #create a var and give it the file text
        return book             #return the text in the var
    except Exception as E:              #I dont know the error for file access, so a general all around type error it is!
        return f"Error Returned as > {E}"               #did I mess up, lets tell me if so.

def count_words(wordcount):             #define the count_words function, accepting the result from get_book_text
    try:                #The 'I probably messed this whole thing up' block
        words = wordcount.split()               #split the book, assign it to words
        num = 0                         #initialize the count to zero
        for i in words:             #begin the loop de loop
            num += 1                #start counting!
        return num                  #finished? ok return the number
    except Exception as E:          #yeah I probably borked it, so lets catch it
        return f"Error Returned as > {E}"               #Tell myself how dumb I am....

def char_count(bookin):
    dict = {}
    for i in bookin:
        i = i.lower()
        dict[i] = dict.get(i,0) + 1
    return dict

def sort_stuff(countin):
    updated_list = []
    for char, count in countin.items():
        if char.isalpha():
            updated_list.append({"char":char, "count": count})
    def sort_on(dict_item):
        return dict_item["count"]
    updated_list.sort(reverse=True, key=sort_on)

            
    return updated_list

def print_fancy_header(text):
    border = "=" * (len(text) + 8)
    print(f"{border}")
    print(f"=== {text} ===")
    print(f"{border}")

def print_fancy_footer():
    footer = "=" * 29
    print(f"{footer} END {footer}")

def print_section_title(title):
    dashes = "-" * (len(title) + 6)
    print(f"{dashes}")
    print(f"-- {title} --")
    print(f"{dashes}")

def print_indented(text, spaces=2):
    indent = " " * spaces
    print(f"{indent}{text}")

