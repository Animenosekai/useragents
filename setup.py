from setuptools import setup
from os import path
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme_description = f.read()
setup(
    name = "pyuseragents",
    packages = ["useragents"],
    version = "1.0",
    license = "MIT",
    description = "A Python module which does one thing: giving you a random User-Agent Header",
    author = "Anime no Sekai",
    author_email = "niichannomail@gmail.com",
    url = "https://github.com/Animenosekai/useragents",
    download_url = "https://github.com/Animenosekai/useragents/archive/v1.0.tar.gz",
    keywords = ['python', 'useragents', 'ua', 'user-agents', 'user-agent', 'http', 'request', 'header', 'http-header'],
    install_requires = [],
    classifiers = ['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 3'],
    long_description = readme_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
)