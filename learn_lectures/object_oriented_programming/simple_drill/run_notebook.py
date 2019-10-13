import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from module_custom.class_note_notebook import Note, NoteBook

new_note = Note()                           # declair OBJECT
quote_book = NoteBook("Very good Word Book")# declair OBJECT

def add_note_notebook(content, page_number):
    new_note.write_content(content)
    quote_book.add_note(new_note.content, page_number=page_number)
    print("Total number of Note are(is)... %d\n" %quote_book.get_number_of_page(),"-"*40+"\n" )

# Direct Add notes -----------------------------
new_note.write_content("Don't cry for me Argentina.. - Song Lyrics")
quote_book.add_note(new_note.content, page_number=5)
print("Total number of Note are(is)... %d\n" %quote_book.get_number_of_page(),"-"*40+"\n" )

# Add notes using function predefined -----------
content = "Another new lylic is needed!"
page_number=7
add_note_notebook(content, page_number)

content = "Hello World!"
add_note_notebook(content, 1)

content = "Are you hungry??"
page_number=3
add_note_notebook(content, 3)

# Show results and Use dict-date ------------------
print(quote_book.notes)
print("Total page: %d / occupied = %s" %(quote_book.get_number_of_page(),quote_book.get_occupied_page()) )
print(quote_book.notes[5][0:5], quote_book.notes[5][17:] )

# Remove dict-date Using pop() function -----------
print()
quote_book.remove_note(5)
print()

# Show results and Use dict-date ------------------
print(quote_book.notes)
print("Total page: %d / occupied = %s" %(quote_book.get_number_of_page(),quote_book.get_occupied_page()) )
# print(quote_book.notes[5][0:5], quote_book.notes[5][17:] )
