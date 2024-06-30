#Task 1:

def add_book(library, title, author): #function to add books to library
    found = False #flag for checking if book to add is already in library
    for book in library: #iterate through the books
        if book[0].lower() == title.lower() and book[1].lower() == author.lower(): #check if titles and authors match in a case-independent manner
            found = True #set flag to true when found
    if found: #check the found flag
        print(f'Sorry "{title}" by {author} is already in the library.') #notify user that that book already exists
    else: #found flag is false
        library.append((title, author)) #append a tuple with the title and author of the book to the library list
        print(f'The title "{title}" by {author} was added to the library') #notify the user that the book was added to the list


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")] #initial library list

print(library) #print initial library
add_book(library, 'Jurrasic Park', 'Michael Chrichton') #add book "Jurassic Park" by Michael Chrichton
add_book(library, '1984', 'George Orwell') #add book "1984" by George Orwell
add_book(library, "Stranger From a Strange Land", "Robert A. Heinlein") #add book "Stranger From a Strange Land" by Robert A. Heinlein
print(library) #print updated library
