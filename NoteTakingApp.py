def add_notes():
  note = input (" Enter your notes:")
  with open ("notes.txt","a") as file:
    file.write(note + "\n")
    print("Notes Added Successfully")

def read_notes():
  with open ("notes.txt","r") as file:
    notes = file.readlines()
    print(notes)
    for note in notes:
      print(f"- {note.strip()}")

while True:
  print("\n Choose Option")
  print("1. Add Notes")
  print("2. Read Notes ")
  print("3. Exit")
  choice = input ("Enter your Choice:")
  if choice == "1":
    add_notes()
  elif choice == "2":
    read_notes()
  elif choice == "3":
    print("Exit")
    break
  else:
    print("Invalid Choice")
