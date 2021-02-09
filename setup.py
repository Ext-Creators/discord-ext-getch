import re
import setuptools


with open("requirements.txt") as stream:
    install_requires = stream.read().splitlines()

with open("discord/ext/getch/__init__.py") as stream:
    version = re.search(r"^version\s*=\s*[\'\"]([^\'\"]*)[\'\"]", stream.read(), re.MULTILINE).group(1)

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

project_urls = {
    "Issue Tracker": "https://github.com/Ext-Creators/discord-ext-getch/issues",
    "Source": "https://github.com/Ext-Creators/discord-ext-getch",
}

setuptools.setup(
    author="Ext-Creators",
    classifiers=classifiers,
    description="Get and Fetch Objects!",
    install_requires=install_requires,
    license="Apache Software License",
    name="discord-ext-getch",
    packages=["discord.ext.getch"],
    project_urls=project_urls,
    python_requires=">=3.7.1",
    url="https://github.com/Ext-Creators/discord-ext-getch",
    version=version,
)
