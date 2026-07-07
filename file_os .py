import os 
import shutil
from pathlib import path 


directory= path(input("Enter the path:")) # Replace with the path to your directory

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],                        
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".rar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []  # For files that don't match any of the above categories
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        
        moved = False
        for category, ext_list in extensions.items():
            if file_extension in ext_list:
                category_dir = os.path.join(directory, category)
                os.makedirs(category_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(category_dir, filename))
                moved = True
                print(f"Moved {filename} to {category}/")
                break
        
        if not moved:
            others_dir = os.path.join(directory, "Others")
            os.makedirs(others_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(others_dir, filename))
            print(f"Moved {filename} to Others/")
    
