from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="excelmind",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An intelligent Excel analysis tool using RAG with natural language processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/excelmind",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Office Suites",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "excelmind=app.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "excelmind": ["data/sample/*"],
    },
)