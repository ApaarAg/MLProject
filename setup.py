from setuptools import find_packages,setup
from typing import List
def get_requirements(path:str)->list[str]:
    # this func will return the required libirary for tthe package
    requirements=[] 

    with open(path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if "-e." in requirements:
            requirements.remove("-e.")
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Apaar",
    author_email='apaaragarwal117@gmail.com',
    packages=find_packages(where='src'),
    package_dir={"":"src"},
    install_requires=get_requirements('requirements.txt')
)