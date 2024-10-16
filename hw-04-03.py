from colorama import Fore, Back, Style
import sys
from pathlib import Path


# parse_folder function accepts absolute path to folder
# to analyze and print structure and indent for each level
# colors:
# folder = GREEN
# file = LIGHTCYAN_EX
#
# used typical file manager output: DIRECTORIES FIRST
# (not default recursive itedir which is accorded to the alphabet simil for files and folders at the same time)


# function accepts path and it's own indent for output
def parse_folder(path: Path, ind: int):

    # check only for top directory for exist, lowers doesn't make any sense to check
    if ind == 0:
        if path.exists() == True:
            print(Fore.GREEN + str(path.name) + "/")
        else:
            Style.RESET_ALL
            print(f"Directory {path} does not exist!")
            return

    # sets for all dirs and files (if any) for current directory
    dirs = set()
    files = set()

    # __fill__ DIRS and FILES
    for el in path.iterdir():
        dirs.add(el) if el.is_dir() else None
        files.add(el) if el.is_file() else None

    # __sort__ DIRS and FILES
    dirs = sorted(dirs)
    files = sorted(files)

    # if we have at least 1 dir: __print it with +4 indent and recourse it__
    if dirs:
        ind += 4
        for d in dirs:
            print(Fore.GREEN + " " * ind + str(d.name) + "/")
            parse_folder(d, ind + 4)

    # if we have at least 1 file: __print it__
    if files:
        for f in files:
            print(Fore.LIGHTCYAN_EX + " " * ind + str(f.name))

    # reset style at the end
    Style.RESET_ALL


# test
def main():

    p = Path(sys.argv[1])
    parse_folder(p, ind=0)


if __name__ == "__main__":
    main()
