
import termcolor   # click on the red bulb and install package

# Importing might not work if the package due to be imported has the same name as a file...
# This python file had the name 'termcolor' so it didn't work
# As soon as I renamed it to 'termcolor_installation' it worked just fine

termcolor.cprint("Hey! this is printed in green!", 'green')
