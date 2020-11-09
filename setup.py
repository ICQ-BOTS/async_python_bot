import io
from os import path

from setuptools import setup, find_packages

import bot

here = path.abspath(path.dirname(__file__))


def long_description():
    with io.open(file=path.join(here, "README.md"), encoding="utf-8") as file:
        return file.read()


def requirements():
    with io.open(file=path.join(here, "requirements.txt")) as file:
        return file.readlines()


setup(
    name="mailru_im_async_bot",
    version=bot.__version__,
    description="Asynchronous Python BOT API library.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/ICQ-BOTS/mailru_im_async_bot",
    author="ICQ LLC (Mail.Ru Group)",
    author_email="support@icq.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent"
    ],
    keywords="mailru im async bot api",
    packages=find_packages(exclude=["example"]),
    install_requires=requirements(),
    python_requires=">= 2.7, != 3.0.*, != 3.1.*, != 3.2.*, != 3.3.*",
    include_package_data=True,
    zip_safe=False
)