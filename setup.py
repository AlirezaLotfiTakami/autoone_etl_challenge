import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoone_etl_challenge",
    version="0.0.1",
    author="Alireza Lotfi",
    author_email="alirezalotfitakami@gmail.com",
    description="Auto one recruitment challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
)