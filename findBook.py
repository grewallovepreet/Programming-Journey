#Check if the book exists in your collection
collectionOfBooks =  ["Mahan Kosh", "War at the top of the world", "Sherlock Holmes" ]
print("Enter the name of book: ")
bookToBeChecked = input()
for book in collectionOfBooks:
  if book == bookToBeChecked:
    print("Yes, I do have the book!")
    break
else:
  print("No, I don't have the book!")
