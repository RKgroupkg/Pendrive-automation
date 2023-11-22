import os
from json_read_module import JSONReader 
import shutil
import tkinter as tk
from tkinter import messagebox
from Auto_keyborad import KeyboardMouseController
import webbrowser

def copy_files(source_folder, destination_folder):
    try:
        # Ensure the source folder exists on the USB drive
        if os.path.isdir(source_folder):
            # Create a subfolder in the destination directory with the source folder name
            destination_subfolder = os.path.join(destination_folder, os.path.basename(source_folder))
            os.makedirs(destination_subfolder, exist_ok=True)

            # List all files in the source folder
            files_to_copy = os.listdir(source_folder)

            if files_to_copy:
                # Copy all files to the subfolder in the destination directory
                for file_name in files_to_copy:
                    source_path = os.path.join(source_folder, file_name)
                    destination_path = os.path.join(destination_subfolder, file_name)
                    shutil.copy2(source_path, destination_path)

                message = f"Files copied successfully to {destination_subfolder}."
                
                if Pop_up == "True":
                    messagebox.showinfo("Success", message)
                else:
                    print(message)
            else:
                message = f"No files found in the source folder '{source_folder}'."
                if Pop_up == "True":
                    messagebox.showwarning("No Files", message)
                else:
                    print(message)
        else:
            message = f"Source folder '{source_folder}' not found."
            if Pop_up == "True":
                    messagebox.showerror("Error", message)
            else:
                print(message)
    except Exception as e:
        message = f"Error copying files: {e}"
        if Pop_up == "True":
            messagebox.showerror("Error", message)
        else:
            print(message)

def main_copy_data(source_folder,destination_folder):
    # Define the source and destination folders
    source_folder = source_folder

    if Pop_up == "True":
        # Create a simple Tkinter window to hide it
        root = tk.Tk()
        root.withdraw()
    else:
        print("NO pop_up")

    # Call the function to copy files
    copy_files(source_folder, destination_folder)

    if Pop_up == "True":
        # Destroy the Tkinter window after processing
        root.destroy()

    # Display completion message
    print("Process completed.")

def open_file_explorer(directory):
    if directory and directory.lower() != "none":
        os.startfile(directory)

def check_user():
    # Get the current username
    current_user = os.getlogin()

    allowed_users = setting.get_value("allowed_users")

    if allowed_users is not None and current_user in allowed_users:
        return False  # User is allowed
    else:
        return True  # User is not allowed




if __name__ == "__main__":
    setting = JSONReader("USB_setting")
    
    if check_user():
        copy = setting.get_value("Copy")
        source_folder = setting.get_value("source_folder")
        destination_folder = setting.get_value("destination_folder")
        if destination_folder == "None":
            destination_folder = os.path.expanduser("~/Downloads")  # User's download directory
        else:
            destination_folder = destination_folder

        Pop_up = setting.get_value("Pop_up")
        Open_explorer = setting.get_value("Open_explorer")
        
        if copy == "True":
            main_copy_data(source_folder,destination_folder)
            if Open_explorer == "True":
                open_file_explorer(destination_folder)
            else:
                print(f"File explorer open :{Open_explorer}")
        else:
            print("not to copy")
        auto_task = KeyboardMouseController(setting)
        auto_task.run()
    else:
        print("user is not allwed to use this feture ")
        
    