import os

def organize_files(directory):
    subdirectories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".txt", ".docx", ".pdf", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Others": []  
    }

    if not os.path.exists(directory):
        print(f"The specified directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            
            destination = None
            for subdirectory, extensions in subdirectories.items():
                if file_extension in extensions:
                    destination = os.path.join(directory, subdirectory)
                    break

            if destination is None:
                destination = os.path.join(directory, "Others")

            if not os.path.exists(destination):
                os.makedirs(destination)

            os.rename(file_path, os.path.join(destination, filename))

def main():
    directory = input("Enter the directory to organize: ")

    print("Organizing files...")
    organize_files(directory)

    print("\nFiles organized into subdirectories:")
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            print(f"- {subdir}")

if __name__ == "__main__":
    main()
