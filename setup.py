import setuptools

setuptools.setup(
    name="crm",
    version="0.0.1",
    url="https://github.com/ardeaf/python-crm",

    author="Ardeaf Lothbrok",
    author_email="ardeaf@gmail.com",

    description="Shitty crm.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
