import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mcl-python",
    version="0.0.2",
    author="Krzysztof Nowak",
    author_email="nowak196@gmail.com",
    description="Python bindings for mcl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fadion96/mcl-python",
    packages=['mcl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
)