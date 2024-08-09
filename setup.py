# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:00:33 2024

@author: Mohamed Tharif
"""

from setuptools import find_packages, setup
from typing import List

HYPHEN_E = "-e ."

def get_requirements(filepath:str)->List[str]:
    '''
    This function return the list of requirements 
    '''
    requirements = []
    with open (filepath, 'r') as file:
        requirements = file.readlines()
        requirements = [x.strip() for x in requirements]

        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return requirements

setup(
    name='Sample_Data_Dashboard',
    version='0.1',
    author= 'Mohamed Tharif',
    author_email= 'mohammedtharif30@gmail.com',
    packages= find_packages(),
    requires= get_requirements('requirements.txt')
)