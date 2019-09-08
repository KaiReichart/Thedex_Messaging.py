import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="Thedex_Messaging",
    version="0.0.2",
    author="Kai Reichart",
    author_email="kai@reichart.dev",
    description="A Package to create Messages for the Thedex_Messaging API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KaiReichart/Thedex-Messaging.py",
    download_url="https://github.com/KaiReichart/Thedex-Messaging.py/archive/v0.0.2.tar.gz",
    packages=setuptools.find_packages(),
    install_requires=[
          'datetime',
      ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
