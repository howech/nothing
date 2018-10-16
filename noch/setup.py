import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="noch",
    version="0.0.1",
    author="howech  ",
    author_email="chris@howeville.com",
    description="howech's do nothing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/howech/nothing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
