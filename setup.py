from setuptools import setup

setup(
    name='md_mermaid',
    version='0.1',
    author='Olivier Ruelle',
    author_email='olivier.ruelle@yahoo.com',
    description='Python-Markdown extension to add support for mermaid graph inside markdown file.',
    url='https://github.com/oruelle/md_mermaid',
    py_modules=['md_mermaid'],
    install_requires = ['markdown>=2.5'],
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
