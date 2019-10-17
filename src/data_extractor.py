from pip._vendor.distlib.compat import raw_input

# UI
optionStart = 1
userInput = ''

print(
    # f"What would you like to do?\n"
    f"Press {optionStart} : To send a request workload data from the server\n"
)

# The length of the input has to be 1 character for the program to work
while ~(userInput.isnumeric() and len(userInput) != 1):
    userInput = raw_input("Please enter your selection from the options listed above: ")
    userInput = userInput.lower()

    if userInput.isnumeric():
        # print(f"Test: Your input was {userInput}")
        break

# UI
