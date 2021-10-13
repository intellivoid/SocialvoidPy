from setuptools import find_packages, setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="socialvoidpy",
    version="0.1.0",
    description="Official socialvoid python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="blank X",
    author_email="blankie@nixnetmail.com",
    url="https://github.com/Intellivoid/SocialvoidPy",
    python_requires=">=3.6",
    include_package_data=True,
    packages=find_packages(exclude=["examples"]),
    install_requires=["httpx==0.20.*", "dataclasses==0.8;python_version<'3.7'"],
)
