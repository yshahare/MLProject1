from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function will returns the requirements
    '''
    requirements=[]
    with open(file_path) as obj:
        requirements=obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author='yogesh',
    author_email='yshahare.mgm@gmail.com',
    package=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
