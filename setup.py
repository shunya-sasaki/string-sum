from setuptools import setup
from setuptools import find_packages
from setuptools_rust import Binding
from setuptools_rust import RustExtension

setup(
    name="string-sum",
    version="1.0",
    rust_extensions=[RustExtension("string_sum", binding=Binding.PyO3)],
    packages=find_packages(),
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
