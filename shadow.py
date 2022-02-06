from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from passgen import passgen
import os

from webdriver_manager.utils import save_file


class bcolors:
    SUCCESS = "\033[92m"  # Green
    FAIL = "\033[91m"  # Red
    RESET = "\033[0m"  # Resets Color
    TITLE = "\033[35m"  # Magenta


def random_users(user_length, numbers_included, save_to_file):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    run = True
    while run:
        random_user = passgen(
            length=user_length,
            punctuation=False,
            digits=numbers_included,
            letters=True,
            case="upper",
        )
        driver.get(f"https://www.tiktok.com/@{random_user}")

        is_user_taken = driver.find_elements_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div/main/div/p[1]'
        )

        verifaction_page = driver.find_elements_by_xpath('//*[@id="verifyEle"]')

        if len(verifaction_page) > 0:
            pass
        elif len(is_user_taken) > 0:
            if save_to_file:
                with open("usernames.txt", "a") as f:
                    if os.stat("usernames.txt").st_size == 0:
                        f.write(f"{random_user}")
                    else:
                        f.write(f"\n{random_user}")
            print(f"{bcolors.SUCCESS}{random_user}{bcolors.RESET}")
        else:
            print(f"{bcolors.FAIL}{random_user}{bcolors.RESET}")


def list_users(save_to_file):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    getting_file = True
    while getting_file:
        file_name = input("\nInput the the text file you want to check: ")

        if os.path.exists(file_name):
            if file_name[len(file_name) - 1] != "t":
                print(f"\n{bcolors.FAIL}ERROR{bcolors.RESET}")
                print("Make sure the file you inputed is a .txt file\n")
            elif file_name[len(file_name) - 2] != "x":
                print(f"\n{bcolors.FAIL}ERROR{bcolors.RESET}")
                print("Make sure the file you inputed is a .txt file\n")
            elif file_name[len(file_name) - 3] != "t":
                print(f"\n{bcolors.FAIL}ERROR{bcolors.RESET}")
                print("Make sure the file you inputed is a .txt file\n")
            elif file_name[len(file_name) - 4] != ".":
                print(f"\n{bcolors.FAIL}ERROR{bcolors.RESET}")
                print("Make sure the file you inputed is a .txt file\n")
            else:
                getting_file = False
        else:
            print(f"\n{bcolors.FAIL}ERROR{bcolors.RESET}")
            print(
                "Please make sure the file you inputed is\n1: Spelled correctly\n2: In the same directory as this python script\n"
            )

    with open(file_name, "r") as f:
        lines = f.readlines()

        driver.get(f"https://www.tiktok.com/@{lines[0]}")
        for line in lines:

            driver.get(f"https://www.tiktok.com/@{line.strip()}")

            is_user_taken = driver.find_elements_by_xpath(
                '//*[@id="main"]/div[2]/div[2]/div/header/div[1]/div[2]/h2'
            )

            if len(is_user_taken) > 0:
                print(f"{bcolors.FAIL}{line.strip()}{bcolors.RESET}")
            else:
                if save_to_file:
                    with open("usernames.txt", "a") as f:
                        if os.stat("usernames.txt").st_size == 0:
                            f.write(f"{line.strip()}")
                        else:
                            f.write(f"\n{line.strip()}")
                print(f"{bcolors.SUCCESS}{line.strip()}{bcolors.RESET}")


def reset_txt_file():
    with open("usernames.txt", "r+") as f:
        f.truncate(0)
    print(f"\n{bcolors.SUCCESS}Reset usernames.txt{bcolors.RESET}")


def update_txt_file():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    with open("usernames.txt", "r") as f:
        lines = f.readlines()

    with open("usernames.txt", "w") as f:
        driver.get(f"https://www.tiktok.com/@{lines[0]}")

        print("\nUpdating...")
        for line in lines:
            driver.get(f"https://www.tiktok.com/@{line.strip()}")

            is_user_taken = driver.find_elements_by_xpath(
                '//*[@id="main"]/div[2]/div[2]/div/header/div[1]/div[2]/h2'
            )

            if len(is_user_taken) == 0:
                f.write(line)

    print(f"\n{bcolors.SUCCESS}Done Updating{bcolors.RESET}")


print(
    f"""{bcolors.TITLE}
 .d8888b.  888                    888                        
d88P  Y88b 888                    888                        
Y88b.      888                    888                        
 "Y888b.   88888b.   8888b.   .d88888  .d88b.  888  888  888 
    "Y88b. 888 "88b     "88b d88" 888 d88""88b 888  888  888 
      "888 888  888 .d888888 888  888 888  888 888  888  888 
Y88b  d88P 888  888 888  888 Y88b 888 Y88..88P Y88b 888 d88P 
 "Y8888P"  888  888 "Y888888  "Y88888  "Y88P"   "Y8888888P"  
                                                                                                                       
{bcolors.RESET}"""
)

print(
    """
 ______________________________
| 1 >> Random Usernames        |
| 2 >> Usernames Off Text File |
| 3 >> Reset Usernames File    |
| 4 >> Update Usernames File   |
|______________________________|
"""
)

with open("usernames.txt", "w"):
    pass
getting_mode = True
while getting_mode:
    mode = input()

    alpha = None
    try:
        int(mode)
    except ValueError:
        print(
            f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nThe mode you inputed is not listed\n"
        )
        alpha = True

    if alpha is None:
        if int(mode) > 0 and int(mode) < 6:
            getting_mode = False
        else:
            print(
                f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nThe mode you inputed is not listed\n"
            )

if int(mode) == 1:
    getting_user_length = True
    while getting_user_length:
        user_length = input("\nWhat length do you want the usernames to be: ")

        alpha = None
        try:
            int(user_length)
        except ValueError:
            print(
                f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nYou can not input non-numaric characters\n"
            )
            alpha = True

        if alpha is None:
            if int(user_length) > 0 and int(user_length) < 25:
                getting_user_length = False
            else:
                print(
                    f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nTiktok only allows usernames under 24 characters\n"
                )

    getting_numbers_include = True
    while getting_numbers_include:
        numbers_included = input("\nDo you want to include number (y/n): ")

        numbers_included = numbers_included.lower()
        if numbers_included == "y":
            numbers_included = True
            getting_numbers_include = False
        elif numbers_included == "n":
            numbers_included = False
            getting_numbers_include = False
        else:
            print(
                f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you only type 'y' or 'n'\n"
            )

    getting_save_to_file = True
    while getting_save_to_file:
        save_to_file = input(
            "\nDo you want to save all unused usernames to usernames.txt (y/n): "
        )

        save_to_file = save_to_file.lower()
        if save_to_file == "y":
            save_to_file = True
            getting_save_to_file = False
        elif save_to_file == "n":
            save_to_file = False
            getting_save_to_file = False
        else:
            print(
                f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you only type 'y' or 'n'\n"
            )

    random_users(int(user_length), numbers_included, save_to_file)

if int(mode) == 2:
    getting_save_to_file = True
    while getting_save_to_file:
        save_to_file = input(
            "\nDo you want to save all unused usernames to usernames.txt (y/n): "
        )

        save_to_file = save_to_file.lower()
        if save_to_file == "y":
            save_to_file = True
            getting_save_to_file = False
        elif save_to_file == "n":
            save_to_file = False
            getting_save_to_file = False
        else:
            print(
                f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you only type 'y' or 'n'\n"
            )

    list_users(save_to_file)

if int(mode) == 3:
    reset_txt_file()

if int(mode) == 4:
    update_txt_file()
