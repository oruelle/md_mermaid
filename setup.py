from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='obsidianhtml_md_mermaid_fork',
    version='0.1.5',
    author='https://github.com/dwrolvink',
    author_email='dwrolvink@protonmail.com',
    description='Bugfix special characters of md_mermaid, because the dev doesn\'t want to fix the bug.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/obsidian-html/md_mermaid',
    py_modules=['obsidianhtml_md_mermaid_fork'],
    install_requires = ['markdown>=2.5'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
