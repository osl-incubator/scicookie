import re
import sys
import os 

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.package_slug}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name."
        "Please do not use a - and use _ instead" % module_name
    )

    # Exit to cancel project
    sys.exit(1)

# Prompt the user for the python_coc variable
python_coc = input("Do you want to include the Python Code of Conduct? (yes/no): ")

# Set the environment variable
os.environ['PYTHON_COC'] = python_coc
