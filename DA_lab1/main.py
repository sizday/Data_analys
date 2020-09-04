import datetime


def answer():
    # function answer; check whether the user wants to correct
    pr_all = False
    pr_ans = False
    while not pr_ans:
        answer = input("1 - Yes, I want fix it\n2 - No, I don't want fix it\n")
        if answer == '1':
            print("Well, the changes are saved")
            pr_all = True
            pr_ans = True
        elif answer == '2':
            print("Incorrect name, enter other")
            pr_all = False
            pr_ans = True
        else:
            print("Enter only 1 or 2")
    return pr_all


def check_name_surname(new_name):
    # function which check name and surname on any errors
    pr_all = True
    right_name = new_name
    err_name = ""
    # check symbols and delete it after function answer
    if not new_name.isalnum():
        t = False
        for i in range(0, len(new_name)):
            if new_name[i] == " ":
                t = True
        if not t:
            right_name = ""
            for i in range(0, len(new_name)):
                if new_name[i].isalnum():
                    right_name += new_name[i]
                    err_name = "Name/surname should consist of letters, digits or gap."
    # check gap and digit in first letter
    if (new_name[0].isdigit()) | (new_name[0] == " "):
        right_name = right_name[1:]
        err_name += " Name/surname can't start on digit and gap."
    while (right_name[0].isdigit()) | (right_name[0] == " "):
        right_name = right_name[1:]
    # autocorrect first letter on title
    if not new_name.istitle():
        right_name = right_name[0].upper() + right_name[1:]
    if err_name != "":
        print("You're wrong.", err_name, "Want to change on", right_name)
        pr_all = answer()
    return pr_all, right_name


def check_number(new_number):
    pr_all = True
    err_name = ""
    # autocorrect +7 on 8
    if new_number[:2] == "+7":
        new_number = "8" + new_number[2:]
    right_number = new_number
    # if first letter is + then error
    if new_number[0] == "+":
        new_number = new_number[1:]
        pr_all = False
        err_name = "'+' can't be a first symbol. "
    # first letter should be 8
    if new_number[0] != "8":
        new_number = "8" + new_number[1:]
        pr_all = False
        err_name = "First number is 8. "
    # check count of number and another error
    if (not new_number.isdigit()) | (not pr_all):
        right_number = ""
        for i in range(0, len(new_number)):
            if new_number[i].isdigit():
                right_number += new_number[i]
        if not new_number.isdigit():
            err_name += "Name should consist only of digits."
        if len(right_number) != 11:
            pr_all = False
            print("You're wrong. Number should consist 11 digits")
        else:
            print("You're wrong.", err_name, "Maybe you mean", right_number)
            pr_all = answer()
    if (len(right_number) != 11) & pr_all:
        pr_all = False
        print("You're wrong. Number should consist 11 digits")
    return pr_all, right_number


def check_data(new_date):
    # function check date
    new_date = new_date.replace(",", " ").replace(":", " ").replace("/", " ").replace(".", " ")
    x = new_date.split()
    pr_all = True
    # check if there are 4th
    if len(x) > 3:
        print("You're wrong.Data should contain 3 parametrs")
        pr_all = False
    # check on digit
    if pr_all:
        for i in range(0, 2):
            if not x[i].isdigit():
                pr_all = False
                if i == 0:
                    print("You're wrong. Day should consist only of digits")
                if i == 1:
                    print("You're wrong. Month should consist only of digits")
                if i == 2:
                    print("You're wrong. Year should consist only of digits")
    # check for existence date
    if pr_all:
        pr_all = False
        day = int(x[0])
        month = int(x[1])
        year = int(x[2])
        if (((month == 1) | (month == 3) | (month == 5) | (month == 7) | (month == 8) | (month == 10) | (month == 12)) &
            (day <= 31)) | (((month == 4) | (month == 6) | (month == 9) | (month == 11)) & (day <= 30)) | (
            (month == 2) & (day <= 28)):
            pr_all = True
        if month == 2 & day == 29 & year % 4 == 0:
            pr_all = True
        if month == 2 & day == 29 & year % 100 == 0:
            pr_all = False
        if month == 2 & day == 29 & year % 400 == 0:
            pr_all = True
        if year < 0:
            pr_all = False
    right_date = x[0] + "." + x[1] + "." + x[2]
    if not pr_all:
        print("You're wrong. No such date")
    return pr_all, right_date


def read_in_line():
    # function which use in another function and return lines_book
    lines_book = []
    for line in open('list_name.txt'):
        lines_book.append(line[:-1])
    return lines_book


def add():
    # function add which add new records
    lines_book = read_in_line()
    new_record = input("Enter new record\nExamples:\nDenis;Sizov;89307014255\nDenis;Sizov;89307014255;19.07.1999\n"
                       "For end of operation you should print 'stop'\n")
    pr_all = True
    pr_repeat = True
    f = open('list_name.txt', "a")
    # to read the tape while 'stop'
    while new_record != 'stop':
        pr_all = True
        f.close()
        f = open('list_name.txt', "a")
        mas_data = new_record.split(";")
        if len(mas_data) != 3 | len(mas_data) != 4:
            print("Incorrect input. Try again.")
            new_record = input("Enter new record: ")
        else:
            new_name = mas_data[0]
            new_surname = mas_data[1]
            new_number = mas_data[2]
            # check date availability
            if len(mas_data) == 4:
                new_date = mas_data[3]
                ch_date = check_data(new_date)
                pr_date = ch_date[0]
                right_date = ch_date[1]
            else:
                pr_date = True
                right_date = ""
            ch_name = check_name_surname(new_name)
            pr_name = ch_name[0]
            right_name = ch_name[1]
            ch_surname = check_name_surname(new_surname)
            pr_surname = ch_surname[0]
            right_surname = ch_surname[1]
            ch_number = check_number(new_number)
            pr_number = ch_number[0]
            right_number = ch_number[1]
            if right_date != "":
                right_date = ";" + right_date
            # check errors on check functions
            if (not pr_name) | (not pr_surname) | (not pr_number) | (not pr_date):
                pr_all = False
                print("A new record is not recorded")
            # check repeat
            if (search(3, right_name + ";" + right_surname) == -1) & (search(3, new_name + ";" + new_surname) == -1):
                pr_repeat = False
            # add records
            if pr_all & (not pr_repeat):
                print("A new record is recorded")
                print(right_name + ";" + right_surname + ";" + right_number + right_date)
                f.write(right_name + ";" + right_surname + ";" + right_number + right_date + "\n")
                lines_book.append(right_name + ";" + right_surname + ";" + right_number + right_date)
                new_record = input("Enter new record: ")
            # repeat function
            if pr_repeat:
                ans = int(input("There is record with such name and surname\nYou want:"
                                "\n1-Change record with such name and surname\n2-Change name and surname in this record"
                                "\n3-Enter next record\n4-Return in menu\n"))
                if ans == 1:
                    name_surname = right_name + ";" + right_surname + ";;"
                    number = search(2, name_surname)
                    lines_book = read_in_line()
                    lines_book[number] = right_name + ";" + right_surname + ";" + right_number + right_date
                    book_str = ''
                    for i in range(len(lines_book)):
                        book_str += lines_book[i] + "\n"
                    print(lines_book[number])
                    open('list_name.txt', 'w').write(book_str)
                    new_record = input("Enter new record: ")
                elif ans == 2:
                    name_surname = input("Enter correct new name and surname: ")
                    new_name = name_surname.split(";")
                    ch_name = check_name_surname(new_name[0])
                    pr_name = ch_name[0]
                    right_name = ch_name[1]
                    ch_surname = check_name_surname(new_name[1])
                    pr_surname = ch_surname[0]
                    right_surname = ch_surname[1]
                    if (not pr_name) | (not pr_surname):
                        print("A new record is not recorded")
                    else:
                        new_record = right_name + ";" + right_surname + ";" + right_number + right_date
                elif ans == 3:
                    new_record = input("Enter new record: ")
                elif ans == 4:
                    new_record = "stop"
            if not pr_all:
                new_record = input("Enter new record: ")


def view():
    # view all records
    lines_book = read_in_line()
    for i in range(len(lines_book)):
        print(lines_book[i])


def delete_all():
    # delete all records
    open('list_name.txt', 'w').close()


def search(mode, search_element):
    # function of search records on some elements
    # mode1 - print; mode2 - return
    if mode == 1:
        search_element = input("Enter field which you want to search, another field remain empty\n"
                               "Example: qwe;;89307014255;\n")
    search_mass = search_element.split(";")
    pr_all = False
    lines_book = read_in_line()
    for i in range(len(lines_book)):
        pr_search = True
        lines_mass = lines_book[i].split(";")
        if len(lines_mass) == 3:
            lines_mass.append("")
        for j in range(len(search_mass)):
            if search_mass[j] != "":
                if search_mass[j] != lines_mass[j]:
                    pr_search = False
        if pr_search:
            pr_all = True
            if mode == 1:
                print("There are no records of such search data")
                print(lines_book[i])
            if mode == 2:
                return i
    if not pr_all:
        return -1


def delete_change_year(mode):
    # function which delete, change, and determines some one element
    # mode1 - delete; mode2 - change; mode3 - count of year
    action = ''
    if mode == 1:
        action = "delete"
    elif mode == 2:
        action = "change"
    elif mode == 3:
        action = "count of year"
    name_surname = input("Enter name and surname record which you want to " + action + "\nExample: Denis;Sizov\n")
    name_surname += ";;"
    number = search(2, name_surname)
    lines_book = read_in_line()
    book_str = ''
    if number != -1:
        if mode == 1:
            print(lines_book[number] + " is deleted")
            del lines_book[number]
        elif mode == 2:
            pr_ans = False
            search_split = lines_book[number].split(";")
            while not pr_ans:
                pr_ans = True
                element = input("What element you want to change\n1-Name\n2-Surname\n3-Number\n4-Birth date\n")
                search_split = lines_book[number].split(";")
                lines_book[number] = ''
                # check correct enter
                if (element != '1') & (element != '2') & (element != '3') & (element != '4'):
                    print("Enter only 1,2,3 or 4")
                    pr_ans = False
                else:
                    new_element = input("Enter new value: ")
                    # check correct of new element by 'check' function
                    if element == '1':
                        pr = check_name_surname(new_element)
                        if pr[0]:
                            search_split[0] = pr[1]
                    elif element == '2':
                        pr = check_name_surname(new_element)
                        if pr[0]:
                            search_split[1] = pr[1]
                    elif element == '3':
                        pr = check_number(new_element)
                        if pr[0]:
                            search_split[2] = pr[1]
                    elif element == '4':
                        pr = check_data(new_element)
                        if pr[0]:
                            if len(search_split) == 4:
                                search_split[3] = pr[1]
                            else:
                                print("This record hasn't date. Do you want to append date?")
                                if answer():
                                    search_split.append(pr[1])
            for i in range(len(search_split)):
                lines_book[number] += search_split[i]
                if i != len(search_split)-1:
                    lines_book[number] += ";"
            print(lines_book[number])
        elif mode == 3:
            print(lines_book[number])
            count_of_year(lines_book, number, 1)
    for i in range(len(lines_book)):
        book_str += lines_book[i] + "\n"
    open('list_name.txt', 'w').write(book_str)


def count_of_year(lines_book, number, mode):
    # function which consider count of year
    # number is sequence number of the line with the required record
    # mode1 - print count of years; mode2 - return count of years; mode3 - more or less than month left to HB
    if number != -1:
        split = lines_book[number].split(";")
        if len(split) == 3:
            if mode == 1:
                print("This record haven't date")
            elif mode == 2:
                return -1
            elif mode == 3:
                return False
        else:
            date = split[3].split(".")
            birth_date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
            birth_date_now = datetime.date(2018, int(date[1]), int(date[0]))
            # now - today date
            now = datetime.date.today()
            pr_before_hb = False
            diff = now - birth_date
            diff_now = now - birth_date_now
            diff_in_year = int(diff.days/365.2425)
            before_hb = int(diff_now.days/30)
            if before_hb == 0:
                pr_before_hb = True
            if mode == 1:
                print("This person have " + str(diff_in_year) + " full years")
            elif mode == 2:
                return diff_in_year
            elif mode == 3:
                return pr_before_hb


def specified_date():
    # function specified date, print day and month - print all such records
    lines_book = read_in_line()
    print("Enter day and month in which you want to show birthday")
    day = input("Day: ")
    month = input("Month: ")
    for i in range(len(lines_book)):
        if i != -1:
            split = lines_book[i].split(";")
            if len(split) == 4:
                date = split[3].split(".")
                if (date[0] == day) & (date[1] == month):
                    print(lines_book[i] + "\n")


def coming_month():
    # function which print all record where birth date in near month
    lines_book = read_in_line()
    print("People, who birthday will less than 1 month:")
    for i in range(len(lines_book)):
        if count_of_year(lines_book, i, 3):
            print(lines_book[i])


def n_year():
    # function which print all records where count of year more/less/equal than N
    n = int(input("Enter N (to view all records by age relative to N): "))
    lines_book = read_in_line()
    more = ''
    less = ''
    equal = ''
    for i in range(len(lines_book)):
        year = count_of_year(lines_book, i, 2)
        if year != -1:
            if year < n:
                less += lines_book[i] + '\n'
            elif year > n:
                more += lines_book[i] + '\n'
            elif year == n:
                equal += lines_book[i] + '\n'
    print("People more than " + str(n) + " years:\n" + more + "People less than " + str(n) + " years:\n"
          + less + "People with " + str(n) + " years:\n" + equal)


def menu():
    # main menu, choose action
    men = input("\nWhat do you want?\n1-View all records\n2-Enter new records\n3-Delete all records\n4-Search record\n"
                "5-Delete only one record\n6-Change only one record\n7-The age of the person\n"
                "8-View all records more/less/equal than N\n9-View all records with birthday in coming month\n"
                "10-View all record with birthday in specified day\n11-Exit\n")
    while men != '11':
        if men == '1':
            view()
        elif men == '2':
            add()
        elif men == '3':
            delete_all()
        elif men == '4':
            search(1, '')
        elif men == '5':
            delete_change_year(1)
        elif men == '6':
            delete_change_year(2)
        elif men == '7':
            delete_change_year(3)
        elif men == '8':
            n_year()
        elif men == '9':
            coming_month()
        elif men == '10':
            specified_date()
        elif men == '11':
            exit(0)
        else:
            print("Incorrect input. Try again")
        men = input("\nWhat do you want?\n1-View all records\n2-Enter new records\n3-Delete all records\n"
                    "4-Search record\n5-Delete only one record\n6-Change only one record\n7-The age of the person\n"
                    "8-View all records more/less/equal than N\n9-View all records with birthday in coming month\n"
                    "10-View all record with birthday in specified day\n11-Exit\n")


menu()
