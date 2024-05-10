from setuptools import setup, find_packages

setup(
    name='mypycountries',
    version='0.1',
    packages=find_packages(),
    description='Simple library to manipulate countries and retrieve geographical data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    author='Julien Mousqueton',
    author_email='julien+github@mousqueton.io',
    url='https://www.ransomware.live',
    license='GNU General Public License v3 (GPLv3)',  
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent', 
    ],
    python_requires='>=3.6',  
    include_package_data=True,  # If you have package data included in MANIFEST.in or specified in package_data
    zip_safe=False,  # Optionally make the package zip safe if there are no requirements for unpacked files
)
