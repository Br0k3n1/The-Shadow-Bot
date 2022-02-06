from heapq import heapify
import shadow as s

class bcolors:
    SUCCESS = "\033[92m"  # Green
    FAIL = "\033[91m"  # Red
    RESET = "\033[0m"  # Resets Color
    TITLE = "\033[35m"  # Magenta


def startup():
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
            numbers_included = input("\nDo you want to include numbers (y/n): ")

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

        getting_thread_amount = True
        while getting_thread_amount:
            thread_amount = input(
                "\nHow many threads do you want to use: "
            )

            if thread_amount.isnumeric() == False:
                print(
                    f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you type a number\n"
                )
            elif int(thread_amount) <= 0:
                print(
                    f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you input a number greater then 0\n"
                )
            else:
                getting_thread_amount = False
        
        getting_hide_chrome = True
        while getting_hide_chrome:
            hide_chrome = input(
                "\nDo you want to hide the chrome window (y/n): "
            )

            hide_chrome = hide_chrome.lower()
            if hide_chrome == "y":
                hide_chrome = True
                getting_hide_chrome = False
            elif hide_chrome == "n":
                hide_chrome = False
                getting_hide_chrome = False
            else:
                print(
                    f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you only type 'y' or 'n'\n"
                )

        s.random_users(int(user_length), numbers_included, save_to_file, thread_amount, hide_chrome)

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
        
        getting_hide_chrome = True
        while getting_hide_chrome:
            hide_chrome = input(
                "\nDo you want to hide the chrome window (y/n): "
            )

            hide_chrome = hide_chrome.lower()
            if hide_chrome == "y":
                hide_chrome = True
                getting_hide_chrome = False
            elif hide_chrome == "n":
                hide_chrome = False
                getting_hide_chrome = False
            else:
                print(
                    f"\n{bcolors.FAIL}ERROR{bcolors.RESET}\nMake sure you only type 'y' or 'n'\n"
                )

        s.list_users(save_to_file, hide_chrome)

    if int(mode) == 3:
        s.reset_txt_file()

    if int(mode) == 4:
        s.update_txt_file()
