# working-tree

Get your beautiful working tree as `yaml` format


## Installation

```shell
pip install working-tree
```

## Usage

- **For current directory**

```python
# some_dir/create_tree.py

from working_tree.tree import make_tree

make_tree()
```

_Then check the `some_dir/working_tree.yaml` file_

- **For specific directory**

```python
# some_dir/create_tree.py

from working_tree.tree import make_tree

make_tree(start_directory="some_subdir/")
```

_Then check the `some_dir/working_tree.yaml` file_

- **With custom output file name**

```python
# some_dir/create_tree.py

from working_tree.tree import make_tree

make_tree(output_file="custom_file_name.yaml")
```

_Then check the `custom_file_name.yaml` file_

## Sample

To see the sample go to the `working_tree/working_tree.yaml` file
