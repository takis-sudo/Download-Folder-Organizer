import os 
import shutil
import fnmatch
import sys


downloaded_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
pdf_path = os.path.join(downloaded_path, 'PDF')
compressed_path = os.path.join(downloaded_path, 'Compressed')
videos_path = os.path.join(downloaded_path, 'Videos')
all_organized_paths = [pdf_path,compressed_path,videos_path]



def organize_dir():
    files = os.listdir(downloaded_path)
    print(f"Found files in {downloaded_path}: {files}")
    for file in files:
        file_path = os.path.join(downloaded_path, file)
        print(f"Processing {file}...")
        if os.path.isfile(file_path):
            if fnmatch.fnmatch(file,'*.rar') or fnmatch.fnmatch(file,'*.zip'):
                print(f"Moved {file} from {file_path} to {compressed_path}")
                shutil.move(file_path, compressed_path)
            elif fnmatch.fnmatch(file,'*.mp4') or fnmatch.fnmatch(file,'*.mkv'):
                print(f"Moved {file} from {file_path} to {videos_path}")
                shutil.move(file_path, videos_path)
            elif fnmatch.fnmatch(file,'*.pdf'):
                print(f"Moved {file} from {file_path} to {pdf_path}")
                shutil.move(file_path, pdf_path)
                

def choose_start():
    user_choice = input("Do you want to organize the folder? (y/n): ")
    while user_choice.lower() not in ("y", "n"):
        print("Invalid input...")
        user_choice = input("Do you want to organize the folder? (y/n): ")
    if user_choice.lower() == "y":
        organize_dir()
    elif user_choice.lower() == "n":
        print("Exiting the program...")
        sys.exit()


if os.path.isdir(pdf_path) and os.path.isdir(compressed_path) and os.path.isdir(videos_path):
    print("Ready to organize the folder.")
    choose_start()
else:
    for directory in all_organized_paths:
        if not os.path.isdir(directory):
            print(f"Creating {directory} folder...")
            os.makedirs(directory)
    choose_start()