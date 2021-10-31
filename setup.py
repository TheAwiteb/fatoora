from setuptools import setup, find_packages

KEYWORD = ["fatoora", "Fatoora", "ZATCA", "QR-Code"]

version = "1.0.1"

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", encoding="utf-8") as require_file:
    requires = [require.strip() for require in require_file]

setup(
    name="fatoora",
    version=version,
    description="An unofficial package help developers to implement ZATCA (Fatoora) QR code easily which required for e-invoicing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TheAwiteb",
    author_email="Awiteb@hotmail.com",
    url="https://github.com/TheAwiteb/fatoora",
    packages=find_packages(),
    license="MIT",
    keywords=KEYWORD,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requires,
)
