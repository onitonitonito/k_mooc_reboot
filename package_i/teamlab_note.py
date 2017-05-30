class Note():       # contains only 1 content per OBJECT.
    def __init__(self, content=None):
        self.content = content

    def __str__(self):
        return self.content

    def write_content(self, content):
        self.content = content

    def remove_all(self):
        self.content = ""


class NoteBook():   # contains title, page_number, notes = { page_number : note.content }
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page_number=0):
        if page_number < 300:
            self.page_number = page_number

            if page_number in self.notes.keys():
                print("*** Error : Sorry!, The page number is already occupied!")
                print("*** The Writing process is aborted! (Failed)")
            else:
                self.notes[self.page_number] = note     # Notes = {1:'content'}
                print("O.K!.. page number {%d} is added!" %(self.page_number,))
                self.page_number +=1
        else:
            print("*** Error : OVER 300!,-- All pages are full!! You can't add any more!!")
            print("*** The Writing process is aborted! (Failed)")

    def remove_note(self,page_number):
        if page_number in self.notes.keys():         # page_number are exist?
            print("O.K!.. page number {%d} is poped out (removed)!" %(page_number,))
            return self.notes.pop(page_number)      # Pop out!
        else:
            print("*** Error : Sorry!, The page number is empty, not available!")
            print("*** Removal process is aborted! (Failed)")

    def get_number_of_page(self):
        return len(self.notes.keys())               # number of data

    def get_occupied_page(self):
        return self.notes.keys()
