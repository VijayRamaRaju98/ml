from setuptools import setup, find_packages
from typing import List

def get_requirements(file:str)->List[str]:
    requirements = []
    HYPEN_E_DOT = '-e .'
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
    name='ml project',
    version='0.0.1',
    author='Vijay',
    author_email='uppalapativijay98@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)