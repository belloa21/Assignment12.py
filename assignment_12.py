# Alex Bello
# 4/23/2020
# Regular Expression Tests

import re

print("Hey, can you please write a string for me?")
user_string = input()
print(user_string)
print("Thanks, now let's run some tests on the string.")

menu = 0

while menu != 11:
    print("""So this menu will let you pick one of many tests to run on your string,
    once you finish one you will be brought back here to either pick another one or leave the menu. 
    Have fun!""")
    print("1. Test your string looking for the letter 'q'.")
    print("2. Test your string to see if it had the word 'the' in it.")
    print("3. Test your string to see if it has an '*' in it.")
    print("4. Test your string to see if it has a digit in it.")
    print("5. Test your string to see if it has a '.' in it.")
    print("6. Test your string to see if it has two consecutive vowels 'a,e,i,o,u' such as the word eat.")
    print("7. Test if your string has white space.")
    print("8. Test if your string has any letters that repeat three times in a single word.")
    print("9. Test if your string starts with the word 'Hello' case sensitive.")
    print("10. Test if your string has an email address in it.")
    print("11. Exit the testing menu.")
    menu = int(input(">"))

    if menu == 1:
        print("Time to check for a 'q'.")
        find = re.findall(r'[q]', user_string)
        if find:
            print("True, which means your string does have a 'q' in it!")
        else:
            print("False, which means your string doesn't have a 'q' in it.")

    if menu == 2:
        print("Time to check if 'the' is in the string.")
        find = re.findall(r'^(the)', user_string)
        if find:
            print("True, which means your string has 'the' in it!")
        else:
            print("False, which means your string doesn't have 'the' in it.")

    if menu == 3:
        print("Time to check for a '*' in the string.")
        find = re.findall(r'\W[*]', user_string)
        if find:
            print("True, which means your string has a '*' in it.")
        else:
            print("False, which means your string doesn't have a '*' in it.")

    if menu == 4:
        print("Time to check for any digits in your string.")
        find = re.findall(r'\d', user_string)
        if find:
            print("True, which means your string has a digit in it!")
        else:
            print("False, which means your string has no digits in it.")

    if menu == 5:
        print("Time to check for a '.' in your string.")
        find = re.findall(r'\.', user_string)
        if find:
            print("True, which means your string has a '.' in it.")
        else:
            print("False, which means your string doesn't have a '.' in it.")

    if menu == 6:
        print("Time to check if your string has two consecutive vowels in it.")
        find = re.findall(r'\w*[aeiou][aeiou]\w*', user_string)
        if find:
            print("True, which means your string has repeating vowels in it!")
        else:
            print("False, which means your string doesn't have repeating vowels in it.")

    if menu == 7:
        print("Time to check if your string has any white space in it.")
        find = re.findall(r'\s', user_string)
        if find:
            print("True, which means your string does have white space in it!")
        else:
            print("False, which means your string doesn't have any white space in it.")

    if menu == 8:
        print("Time to check if your string has any words with triple repeating letters in it.")
        find = re.findall(r'\w{3}\w{3}', user_string)
        if find:
            print("True, which means that your string has a word that has three letters repeating in it!")
        else:
            print("False, which means your string doesn't have a word that has three letters repeating in it.")

    if menu == 9:
        print("Time to check if your string starts with 'Hello' with an upper case H.")
        find = re.findall(r'^Hello', user_string)
        if find:
            print("True, which means your string starts with Hello with an upper case 'H'!")
        else:
            print("False, which means your string doesn't start with Hello with a upper case 'H'.")

    if menu == 10:
        print("Time to check if your string has an email address in it.")
        find = re.findall(r'\w+@\w+\.\w+', user_string)
        if find:
            print("True, which means your string contains an email address!")
        else:
            print("False, which means your string doesn't contain an email address.")
