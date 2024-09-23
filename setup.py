import setuptools
from setuptools import find_packages

with open("README.md",'r',encoding = "utf-8") as f:
    description = f.read()


__version__ = "0.0.0"

REPO_NAME = 'End-to-End-Deep-Learning-Project'
AUTHOR_USER_NAME = "LalitMahale"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = 'lalitmahale121@gmail.com'


setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description= description,
    long_description_content = "text/markdown",
    url = "https://github.com/LalitMahale/End-to-End-Deep-Learning-Project",
    project_urls = {
        "Bug Tracker":  f"https://github.com/LalitMahale/End-to-End-Deep-Learning-Project/issue"},
    
    package_dir={"":"src"},
    packages=setuptools.find_packages(where= "src")
    
    )