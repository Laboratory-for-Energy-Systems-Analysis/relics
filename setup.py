from setuptools import setup

v_temp = {}
with open("relics/version.py") as fp:
    exec(fp.read(), v_temp)
version = ".".join((str(x) for x in v_temp["version"]))


setup(
    name="relics",
    version=version,
    packages=[
        "relics",
    ],
    author="Romain Sacchi",
    author_email="romain.sacchi@psi.ch",
    license="BSD 3-clause",
    package_data={"relics": ["data/*.xlsx", "data/*.json"]},
    install_requires=["bw2io", "bw2data", "requests", "pyyaml", "numpy<2.0.0"],
    url="https://github.com/romainsacchi/relics",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    description="Import life-cycle assessment indicators for Brightway for assessing resource extraction",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
