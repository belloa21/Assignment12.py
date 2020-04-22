# Alex Bello
# 4/23/2020
# Regular Expression Tests

print("Hey, can you please write a string for me?")
input()
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
    menu = int(input(">"))


