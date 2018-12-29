import setuptools

setuptools.setup(
    name='tlen',
    version='1.0',
    author='Tomasz Łoś',
    author_email='tloszabno@gmail.com',
    description='A tool to learn foreign language',
    packages=["tlen"],
    entry_points={
        'console_scripts': [
            'tlen = tlen.main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)