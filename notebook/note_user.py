from teamlab_note import Notebook
from teamlab_note import Note

new_note = Note()
new_note.write_content("Don't cry because it's over, smile because it happend. - Dr. Seuss")

quote_book = Notebook("The Quote Book")
quote_book.add_note(new_note, 10)
quote_book.add_note(new_note)
quote_book.add_note(new_note)
quote_book.add_note(new_note)
quote_book.add_note(new_note)
quote_book.add_note(new_note)
print(quote_book.get_number_of_pages())

my_note = quote_book.remove_note(10)
print(my_note)

my_note = quote_book.remove_note(10)
print(my_note)
