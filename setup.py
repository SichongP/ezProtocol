import setuptools

with open("README.md","r") as fh:
	long_des = fh.read()

setuptools.setup(
    name="ezProtocol",
    version="0.0.1",
    author="Sichong Peng",
    author_email="scpeng@ucdavis.com",
    description="a protocol writer for opentrons OT-2 robot",
    long_description=long_des,
    long_description_content_type="text/markdown",
    url="https://github.com/SichongP/ezProtocol",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['ezprotocol = ezProtocol.__main__:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['python-frontmatter','pandas','PyYAML','regex','opentrons>3']
)
