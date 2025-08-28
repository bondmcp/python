from setuptools import setup, find_packages

setup(
    name="bondmcp-cli",
    version="1.0.0",
    description="Official BondMCP CLI and Python SDK",
    long_description="Command-line interface and Python SDK for the BondMCP health AI platform",
    author="BondMCP Team",
    author_email="support@bondmcp.com",
    url="https://github.com/auroracapital/bondmcp-python",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "click>=8.0.0",
        "pydantic>=1.8.0",
        "python-dotenv>=0.19.0"
    ],
    entry_points={
        'console_scripts': [
            'bondmcp=bondmcp.cli:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
