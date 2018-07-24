'''
setup for pypi package
'''
from setuptools import setup


setup(
    name='xcut',
    version='0.0.5',
    python_requires='>=3.6.1',

    packages=[],
    # py_modules=['xcut'], # single module
    install_requires=[],
    scripts=['xcut'],
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
