import pathlib


# get_cats_info function accepts relative path to cats info text file
# and return list of dicts with all information
# or
# error in string if something goes wrong


def get_cats_info(filename: str) -> dict:

    # find path to our .py scrypt file
    current_dir = pathlib.Path(__file__).parent

    try:
        # trying to open file in current directory and read all the lines without "\n" signatures
        with open(current_dir / filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

            # variables for result: dict "cat" for single one and list "cats" for all
            cat = {}
            cats = []

            # fill dict for single cat by predefined keys
            # and values as splitting string
            for one_line in lines:
                keys = ["id", "name", "age"]
                values = one_line.split(",")
                cat = dict(zip(keys, values))
                cats.append(cat)

    except Exception as e:
        return str(e) + " error in get_cats_info()"

    return cats


# test
def main():
    print(get_cats_info("hw-04-02-cats.txt"))


if __name__ == "__main__":
    main()
