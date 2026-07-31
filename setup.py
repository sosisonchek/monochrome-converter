from setuptools import setup

setup(
    name="monochrome-converter",
    version="1.0",
    py_modules=["init", "main"],
    install_requires=[
        "Pillow",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "monochrome=main:main",
        ],
    },
)