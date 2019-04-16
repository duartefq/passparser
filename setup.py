import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitpassparser-test",
    version="0.0.1",
    author="Duarte Fernandes",
    author_email="duartefq@outlook.com",
    description="A package to parse and sanitize passwords from Bitwarden",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duartefq/passparser",
    packages=setuptools.find_packages(),
    scripts=['bin/bitpassparser'],
    install_requires=['tldextract'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
