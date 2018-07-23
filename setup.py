'''
setup for pypi package
'''
from setuptools import setup

version = "0.0.1"

setup(
    name='xcut',
    version = version,
    python_requires='>=3.6.1',

    packages=[],
    #py_modules=['xcut'], # single module
    install_requires=[ ],
    scripts = ['xcut'],
    description = open('README.md').readlines()[1],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = "ahuigo",
    author_email = "ahui132@qq.com",
    license = "MIT",
    url = "http://github.com/ahuigo/xcut",
)

