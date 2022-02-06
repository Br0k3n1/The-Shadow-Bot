from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from passgen import passgen
import os
import threading
import startup as s

from webdriver_manager.utils import save_file


class bcolors:
    SUCCESS = "\033[92m"  # Green
    FAIL = "\033[91m"  # Red
    RESET = "\033[0m"  # Resets Color
    TITLE = "\033[35m"  # Magenta

def random_users(user_length, numbers_included, save_to_file, thread_amount, hide_chrome):
    thread_amount = int(thread_amount)
    def do_request():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        if hide_chrome:
            driver.set_window_position(-10000,0)
        
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
        
    threads = []

    for i in range(thread_amount):
        t = threading.Thread(target=do_request)
        t.daemon = True
        threads.append(t)
    for i in range(thread_amount):
        threads[i].start()
    for i in range(thread_amount):
        threads[i].join()


def list_users(save_to_file, hide_chrome):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    if hide_chrome:
        driver.set_window_position(-10000,0)

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
    driver.set_window_position(-10000,0)
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
    driver.close()

    print(f"\n{bcolors.SUCCESS}Done Updating{bcolors.RESET}")


if __name__ == "__main__":
    s.startup()
