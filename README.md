# string-sum python package

Python package which is written with Rust.
This project is my tutorial to create a python package with Rust.


## How to build

```shell
python -m pip install build
python -m build
```


## Usage

```python
import string_sum

a = 2
b = 3

result = string_sum.sum_as_string(a, b)
print(result)
```

The output is the following.

```
'5'
```


## Author

Shunya Sasaki &lt;shunya.sasaki1120@gmail.com&gt;
