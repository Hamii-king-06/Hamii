from setuptools import setup, find_packages

setup(
    name="Hamii",
    version="0.1.0",
    description="Simple terminal color formatting with easy {color} placeholders",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="YourName",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="terminal color ansi formatting",
)
