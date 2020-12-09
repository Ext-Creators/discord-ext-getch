import re
import setuptools


with open("README.rst", "r") as f:
    long_description = f.read()

with open("requirements.txt") as stream:
    install_requires = stream.read().splitlines()

with open("discord/ext/template/__init__.py") as f:
    version = re.search(r"^version\s*=\s*[\'\"]([^\'\"]*)[\'\"]", f.read(), re.MULTILINE).group(1)

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
    "Issue Tracker": "https://github.com/Ext-Creators/discord-ext-template/issues",
    "Source": "https://github.com/Ext-Creators/discord-ext-template",
}

setuptools.setup(
    author="Ext-Creators",
    classifiers=classifiers,
    description="The repository description.",
    install_requires=install_requires,
    license="Apache Software License",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    name="discord-ext-template",
    packages=["discord.ext.template"],
    project_urls=project_urls,
    python_requires=">=3.5.3",
    url="https://github.com/Ext-Creators/discord-ext-template",
    version=version,
)
