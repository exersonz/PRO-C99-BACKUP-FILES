import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = input("Enter the path to delete: ")
    #days = 30
    seconds = time.time() - 3
    #seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        print("The path exists")
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))

        fileOrFolderAge = os.stat(path).st_ctime
        #print("fileOrFolderAge = " + format(fileOrFolderAge))
        #print("seconds = " + format(seconds))

        for file in files:
            file_path = os.path.join(root, file)

            if seconds > fileOrFolderAge:
                #print("fileOrFolderAge <= seconds, seconds - fileOrFolderAge = " + format(seconds - fileOrFolderAge))
                print("File removed successfully :)")
                os.remove(file_path)
                deleted_files_count += 1
            else:
                #print("fileOrFolderAge > seconds, fileOrFolderAge - seconds = " + format(fileOrFolderAge - seconds))
                print("Files or folders are too young to delete >:)")
        print(f"Total number of files deleted: {deleted_files_count}")

        for folder in dirs:
            folder_path = os.path.join(root, folder)

            if seconds > fileOrFolderAge:
                #print("fileorFolderAge <= seconds, seconds - fileOrFolderAge = " + format(seconds - fileOrFolderAge))
                print("Folder removed successfully :)")
                shutil.rmtree(folder_path)
                deleted_folders_count += 1

            else:
                #print("fileOrFolderAge > seconds, fileOrFolderAge - seconds = " + format(fileOrFolderAge - seconds))
                print("Files or folders are too young to delete >:)")
        print(f"Total number of folders deleted: {deleted_folders_count}")

    else:
        print("The path doesn't exist")
main()