## File Management System

import os
import shutil
import time

def main():
    while True:
        print("Welcome to the File Management System")
        print("1. Create a new file")
        print("2. Read a file")
        print("3. Write to a file")
        print("4. Delete a file")
        print("5. Copy a file")
        print("6. Move a file")
        print("7. Rename a file")
        print("8. List all files in a directory")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            write_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            copy_file()
        elif choice == 6:
            move_file()
        elif choice == 7:
            rename_file()
        elif choice == 8:
            list_files()
        elif choice == 9:
            print("Exiting...")
            time.sleep(2)
            exit()
        else:
            print("Invalid choice. Please try again.")
            main()

def create_file():
    filename = input("Enter the name of the file: ")
    with open(filename,
                "w") as file:
            print("File created successfully")

def read_file():
    filename = input("Enter the name of the file: ")
    with open(filename, "r") as file:
        print(file.read())

def write_file():
    filename = input("Enter the name of the file: ")
    print(filename)
    content = input("Enter the content to be written: ")
    with open(filename,"w") as file:
            file.write(content)
            print("Content written successfully")

def delete_file():
    filename = input("Enter the name of the file: ")
    os.remove(filename)
    print("File deleted successfully")

def copy_file():
    source = input("Enter the name of the source file: ")
    destination = input("Enter the name of the destination file: ")
    shutil.copy(source, destination)
    print("File copied successfully")

def move_file():
    source = input("Enter the name of the source file: ")
    destination = input("Enter the name of the destination file: ")
    shutil.move(source, destination)
    print("File moved successfully")

def rename_file():
    old_name = input("Enter the name of the file to be renamed: ")
    new_name = input("Enter the new name of the file: ")
    os.rename(old_name, new_name)
    print("File renamed successfully")


def list_files():
    path = input("Enter the path of the directory: ")
    files = os.listdir(path)
    print("Files in ", path)
    for file in files:
        print(file)

if __name__ == "__main__":
    main()






    