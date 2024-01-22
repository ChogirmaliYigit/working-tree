from setuptools import setup


setup(
    name='working_tree',
    version='0.0.1b4',
    license='MIT',
    author="Jahongir Ibragimov",
    author_email='chogirmali.yigit@gmail.com',
    packages=['working_tree'],
    url='https://github.com/ChogirmaliYigit/working-tree',
    keywords='working tree',
    install_requires=[
        'gitignore-parser==0.1.11',
        "pyyaml==6.0.1",
    ],
)
