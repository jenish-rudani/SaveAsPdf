import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-saveaspdf-jenishRudani",  # Replace with your own username
    version="0.1",
    author="Jenish Rudani",
    author_email="jrudani1999@gmail.com",
    description="Save Multiple Webpage As PDF",
    long_description=Script_to_save_Multiple_Webpage_As_PDF,
    long_description_content_type="text/markdown",
    url="https://github.com/JenishRudani98/SaveAsPdf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
