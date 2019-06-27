from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='md_mermaid',
    version='0.1',
    author='Olivier Ruelle',
    author_email='olivier.ruelle@yahoo.com',
    description='Python-Markdown extension to add support for mermaid graph inside markdown file.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/oruelle/md_mermaid',
    py_modules=['md_mermaid'],
    install_requires = ['markdown>=2.5'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: GNU GPLv3',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
