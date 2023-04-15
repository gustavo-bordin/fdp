import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FDP",
    version="0.0.1",
    author="Gustavo Bordin",
    author_email="self.bordin@gmail.com",
    description="FDP - A PDF extractor programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gustavo-bordin",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    entry_points = {
        "console_scripts" : [
            "fdp=fdp.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    keywords = "python programming-language interpreter pdf",
    python_requires='>=3.6',
)