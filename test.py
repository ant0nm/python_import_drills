# importing a function from a module in the root directory
from ascii import one, two
# importing functions from a module inside a package in the root directory
from art.pictures import three, four
# importing functions from a module inside nested packages
from art.even_more_art.images import five
# importing a function from a module in the root directory
from scene import six

# test all the imported functions
print(one(), two(), three(), four(), five(), six(), sep="\n\n\n")
