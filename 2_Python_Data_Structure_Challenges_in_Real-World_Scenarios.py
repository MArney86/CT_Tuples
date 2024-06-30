#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

#Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

def add_book(library, title, author):
    found = False
    for book in library:
        if book[0].lower() == title.lower() and book[1].lower() == author.lower():
            found = True
    if found:
        print(f'Sorry "{title}" by {author} is already in the library.')
    else:
        library.append((title, author))
        print(f'The title "{title}" by {author} was added to the library')


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

print(library)
add_book(library, 'Jurrasic Park', 'Michael Chrichton')
add_book(library, '1984', 'George Orwell')
add_book(library, "Stranger From a Strange Land", "Robert A. Heinlein")
print(library)
