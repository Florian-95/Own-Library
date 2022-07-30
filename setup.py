import setuptools

setuptools.setup(
    name="packageFlo",
    version="1.0.0",
    author="Florian",
    description="Own Python package.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
