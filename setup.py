'''
setup for pypi package
'''
from setuptools import setup

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        import sys
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='xcut',
    version='0.0.8',
    python_requires='>=3.6.1',

    packages=[],
    # py_modules=['xcut'], # single module
    install_requires=[
        'click',
        ],
    scripts=['xcut'],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},

    description=open('README.md').readlines()[1].strip(),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="ahuigo",
    author_email="ahui132@qq.com",
    license="MIT",
    url="http://github.com/ahuigo/xcut",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ],

)
