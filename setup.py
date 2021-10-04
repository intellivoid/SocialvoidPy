from setuptools import find_packages, setup
import socialvoidpy

with open("README.md") as file:
    long_description = file.read()

setup(
    name="socialvoidpy",
    version=socialvoidpy.__version__,
    description="Official socialvoid python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="blank X",
    author_email="blankie@nixnetmail.com",
    url="https://github.com/Intellivoid/SocialvoidPy",
    python_requires=">=3.6",
    include_package_data=True,
    packages=find_packages(exclude=["examples"]),
    install_requires=["httpx==0.19.*", "dataclasses==0.8"],
)
