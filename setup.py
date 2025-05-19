from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_req(file_path:str)->List[str]:
    '''
    This function brings all the requirements from the requirement.txt in the form of a list
    '''
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name="MLproject",
    version='0.0.1',
    author='Dhruv',
    author_email='dhruvsandhu21@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)