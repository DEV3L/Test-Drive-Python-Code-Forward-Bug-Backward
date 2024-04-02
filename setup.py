from setuptools import find_packages, setup

setup(
    name="python-code-blog-posts",
    version="0.1",
    description="Example repository to go with blog posts that have Python related code examples.",
    author="Justin Beall",
    author_email="jus.beall@gmail.com",
    packages=find_packages(),  # Automatically discover all packages
    install_requires=["networkx"],
    extras_require={"dev": ["black", "isort", "pytest", "pytest-cov", "pylint"]},
)
