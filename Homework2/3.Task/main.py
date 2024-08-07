import sys
from colorama import Fore, init, Back
from pathlib import Path

init(autoreset=True)


def show_directory_files(path=sys.argv):

    try:
        # check if path was entered
        if len(path) <= 1:
            raise ValueError

        # pull out the folder
        dest_dir = Path(path[1])

        # check if the folder is exist
        if not dest_dir.exists():
            raise FileExistsError

        # check if it's a directory
        if dest_dir.is_dir():
            list_of_files = []
            #sort files in the way they are appears in the folder
            for el in sorted(
                dest_dir.iterdir(), key=lambda e: (e.is_file(), e.is_dir())
            ):
                #if the path is directory we goes inside and pull out the files
                # added them after the directory where they were.
                if el.is_dir():
                    parent_folder_name = el.name
                    list_of_files.append(el)
                    for file in el.glob("**/*"):
                        if parent_folder_name in file.parts:
                            list_of_files.append(file)
                else:
                    list_of_files.append(el)

            # show list of files inside the directory.
            print("📦 " + Back.YELLOW + str(dest_dir.name))
            for path in list_of_files:
                if path.is_dir():
                    print("📁 " + Back.LIGHTCYAN_EX + str(path.name))
                else:
                    print("📜 " + Fore.GREEN + str(path.name))
        else:
            print(Fore.RED + "Sorry, but thats's not a directroy")
    except FileExistsError:
        print(Fore.RED + f"the {path} doesn't exist")
    except ValueError:
        print(Fore.RED + f"Path if required!")


if __name__ == "__main__":
    show_directory_files()
