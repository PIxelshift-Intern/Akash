
# Mandatory Hello World
print("Hello World")

##
# 
# How does this work?
# The is compiled and run through the python interpreter, this is not directly compiled to machine code 
# but to byte code which is then run by the python interpreter
# 
# this is a simple print statement which prints the string "Hello World" to the console
# 
# 
# 
# #

# %% Virtual Environment Management without Poetry(package manager)
# This can cause various issues like dependency conflicts, versioning issues, etc.
"""
Virtual Environment Workflow:
1. Install: pip install virtualenv
2. Create environment: virtualenv env_name
3. Activate environment: source env_name/bin/activate
4. Deactivate environment: deactivate
5. Install dependencies: pip install package_name
6. Export dependencies: pip freeze > requirements.txt
7. Install from requirements.txt: pip install -r requirements.txt
"""


# %% Virtual Environment Management with Poetry
# Poetry is a python dependency management and packaging tool
# Others are present but mostly will be using poetry {if need be will use others}
"""
Poetry Workflow:
1. Install: pip install poetry
2. Create project: poetry new project_name
3. Create environment: poetry env use python3.x
4. Add dependencies: poetry add package_name
5. Install from pyproject.toml: poetry install
6. Activate environment: poetry shell
7. Run scripts: poetry run python script.py
"""