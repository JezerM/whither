# Always prefer setuptools over distutils
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='whither',
    version='0.3.4',
    packages=[
        'whither',
        'whither.base',
        'whither.toolkits',
        'whither.toolkits.qt',
        'whither.toolkits.gtk',
    ],
    url='https://github.com/JezerM/whither',
    license='GPL-3.0',
    author='Antergos Linux Project',
    author_email='dustin@antergos.com',
    description='Desktop application SDK for creating Universal Linux Applications.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'PyQt5',
        'ruamel.yaml',
    ],
    package_data={
        '': ['whither.yml'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
    ],
    keywords='desktop-application-sdk framework sdk javascript universal html5'
)
