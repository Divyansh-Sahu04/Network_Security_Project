"""
The setup.py file is an essential part of packaging and
distributing Python projects. It is used by setuptools
(or disutils in older Python versions) to define the config
of your projects such as metadata, dependencies and more       
"""

from setuptools import find_packages,setup
from typing import List
"""
what find packages is going to do is it is going to scan all the folders
and wherever there is __init__.py file it will consider as a package
"""
"""
Setup is responsible to provide all the information about the project
-e . triggers the setup file
"""


HYPEN_E_DOT="-e ."
def get_requirements()-> List[str]:
    # this function return the list of requiremnets
    requirements_lst:list[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements!=HYPEN_E_DOT:
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirements_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Divyansh Sahu",
    author_email="skills.divyansh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

    