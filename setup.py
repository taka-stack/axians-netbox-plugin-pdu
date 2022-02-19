
from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='axians-netbox-plugin-pdu',
#    version='0.0.4',
    url='https://github.com/taka-stack/axians-netbox-plugin-pdu',
#    download_url='https://github.com/taka-stack/axians-netbox-plugin-pdu/archive/v0.9.2.tar.gz',
    description='A topology visualization plugin for Netbox powered by NextUI Toolkit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alexander Gittings',
    author_email='alexander.gittings@axians.co.uk',
    install_requires=[],
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    keywords=['axians','netbox', 'netbox-plugin', 'plugin','pdu'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
