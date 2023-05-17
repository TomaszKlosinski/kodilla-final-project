import setuptools
setuptools.setup(
    name='blog',
    version='1.0',
    packages=setuptools.find_packages(exclude=['tests']),
    long_description='Blog app',
    python_requires='>=3.10',
    install_requires=[
        'flask',
        'flask-migrate',
        'requests',
    ]
)
