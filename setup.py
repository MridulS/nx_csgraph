from setuptools import find_packages, setup

extras_require = {
    "test": ["pytest", "scipy"],
}

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")
with open("README.md") as f:
    long_description = f.read()

setup(
    name="nx-csgraph",
    version="0.0.1",
    entry_points={'networkx.plugins': 'nxcsgraph = nx_csgraph.interface:Dispatcher'},
    description="A PoC from NetworkX plugin with sparse.csgraph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mridul Seth",
    author_email="mail@mriduls.com",
    url="https://github.com/mriduls/nx_csgraph",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    license="Apache License 2.0",
    keywords=[
        "graph",
        "sparse",
        "matrix",
        "Networks",
        "Graph Theory",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
