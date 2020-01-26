# mcl-python

`mcl-python` is a Python library that creates bindings for [mcl](https://www.google.com) library by [herumi](https://github.com/herumi).

## Installation
For now `mcl-python` supports Linux only.
### Requirements
- Preinstalled [mcl](https://www.google.com) library
### How to install
To install mcl-python use package manager [pip](https://pip.pypa.io/en/stable/)
```
pip install mcl-python
```
And set mcl installation dir to `MCL_PATH` environment variable
```
export MCL_PATH=<path_to_mcl>
```
## Usage
```python
import mcl

mcl.mcl_init(mcl.CurveType.MCL_BLS12_381))

sk = mcl.Fr()
sk.set_by_CSPRNG()
print(sk)
```
## License
[LICENSE](https://github.com/Fadion96/mcl-python/blob/master/LICENSE)