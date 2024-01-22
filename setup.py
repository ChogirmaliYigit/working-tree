from setuptools import setup, find_packages


setup(
    name='working-tree',
    version='0.0.1b0',
    license='MIT',
    author="Jahongir Ibragimov",
    author_email='chogirmali.yigit@gmail.com',
    packages=find_packages('working-tree'),
    package_dir={'': 'working-tree'},
    url='https://github.com/ChogirmaliYigit/working-tree',
    keywords='working tree',
    install_requires=[
        'gitignore-parser==0.1.11',
        "pyyaml==6.0.1",
    ],
)
