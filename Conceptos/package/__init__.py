# The time has come to introduce the magic of the __init__.py file.
# This file, although it may seem unassuming, is crucial to defining a Python package.
# Let's explore its role in initializing our package and offering our modules to the world.

print("Initializing the package...")

# The __init__.py file can include imports to expose specific functionality to the package user.
# By adding imports here, we make those modules accessible directly via the package.

# For example, suppose we have two modules: 'math_operations.py' and 'file_handler.py'.
# The following import statements will make them part of the package namespace.

from .math_operations import (
    add,
    subtract,
)  # Importing specific functions from math_operations
from .file_handler import read_file, write_file  # Importing functions from file_handler

# This means that when someone imports this package, they can directly access these functions:
# - from package_name import add, subtract
# - from package_name import read_file, write_file

# We could also define package-level variables or settings here.

__all__ = [
    "add",
    "subtract",
    "read_file",
    "write_file",
]  # Defining what is exposed to users

# __all__ is a list of public objects of the module or package. It restricts what is imported
# when 'from package import *' is used, ensuring that only the defined elements are imported.

# You may also initialize some data or configurations for the package. For example:

package_version = "1.0.0"  # Defining the version of the package, this varible will be globably interpreted


def show_version():
    print(f"Package version: {package_version}")


# This function is available throughout the package and can be accessed as follows:
# - from package_name import show_version

# Finally, it's possible to perform setup or logging tasks for the package when it's imported.
# For example, initializing logging for the package:

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Package initialized successfully!")
