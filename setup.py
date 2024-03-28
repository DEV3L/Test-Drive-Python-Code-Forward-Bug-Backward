from setuptools import find_packages, setup

setup(
    name="Test-Drive-Python_Code-Forward-Bug-Backward",
    version="0.1",
    description="Example repository to go with blog post on Test-Drive Python Code Forward, Bug Backward.",
    author="Justin Beall",
    author_email="jus.beall@gmail.com",
    packages=find_packages(),  # Automatically discover all packages
    install_requires=["openai", "python-dotenv", "sqlalchemy"],
    extras_require={"dev": ["black", "isort", "pytest", "pytest-cov", "pylint"]},
)
