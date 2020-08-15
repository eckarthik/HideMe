import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hideme", # Replace with your own username
    version="0.0.5",
    author="Karthik E C",
    author_email="eckarthik39@gmail.com",
    description="A Python package to fetch usable proxies from the internet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eckarthik/HideMe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'hideme': ['user_agents.txt']},
    include_package_data=True,
    python_requires='>=3.0',
)