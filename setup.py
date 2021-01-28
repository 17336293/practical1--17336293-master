from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Christopher Doyle",
      author_email="christopher.doyle1@ucd.ie",
      install_requires = ['psutil'],
      packages=['systeminfo'],
      entry_points={
        'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
        }
      )

#Importnat info, requirements, as it states what external packages are needed to function
