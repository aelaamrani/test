import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='test',
    version='1.0.0',
    author='Ahmed El Aamrani',
    author_email='ahmed.elaamrani@underarmour.com',
    description='Test Pacage',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aelaamrani/tests',
    project_urls = {
        "Bug Tracker": "https://github.com/aelaamrani/test/issues"
    },
    # license='MIT',
    packages=['test'],
    install_requires=['pandas'],
)