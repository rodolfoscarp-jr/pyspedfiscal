from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='pyspedfiscal',
    version='0.1.0',
    url='',
    license='MIT License',
    author='Rodolfo Scarp',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='rodolfoscarp@gmail.com',
    keywords='spedfiscal',
    description=u'Serializa um arquivo do tipo SPED Fiscal',
    packages=['pacotepypi'],
    install_requires=['pydantic']
)
