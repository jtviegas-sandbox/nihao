import logging
import os

from setuptools import setup, find_namespace_packages

logger = logging.getLogger(__name__)
VERSION = "0.0.2"

version = os.getenv("TGEDR_NIHAO_VERSION", VERSION)

logging.info(f"[tgedr-nihao] building version: {version}")

setup(
    name='tgedr-nihao',
    version=version,
    description='This package provides code derived from studies with financial data sources',
    url='https://github.com/jtviegas-sandbox/nihao',
    author='joao tiago viegas',
    author_email='jtviegas@gmail.com',
    license='Unlicense',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
    ],
    keywords='finance development data science',
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        "yfinance==0.2.31",
    ],
    python_requires='>=3.7',
    # package_data={'sample': ['package_data.dat'],},
)
