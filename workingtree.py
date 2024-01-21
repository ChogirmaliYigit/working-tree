import os
import yaml
from gitignore_parser import parse_gitignore


def create_yaml_tree(directory, gitignore=None, level=0):
    tree = {}

    # Get the list of items in the directory
    items = os.listdir(directory)

    if gitignore:
        # Parse the .gitignore file
        gitignore_parser = parse_gitignore(gitignore)

        # Filter out items listed in .gitignore
        items = [item for item in items if not gitignore_parser(item)]

    for item in items:
        # Exclude hidden files and directories (starting with dot)
        if not item.startswith('.'):
            path = os.path.join(directory, item)

            if os.path.isdir(path):
                # Recursively call for subdirectories
                tree[item] = create_yaml_tree(path, gitignore, level + 1)
            else:
                tree[item] = None  # Leaf node (file)

    return tree


def save_yaml(tree, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(tree, file, default_flow_style=False)


if __name__ == "__main__":
    # Specify the directory you want to start the tree from
    start_directory = '.'  # Current working directory

    # Specify the .gitignore file if present
    gitignore_file = '.gitignore'

    # Specify the output YAML file
    output_yaml_file = 'working_tree.yaml'

    if os.path.exists(gitignore_file):
        tree = create_yaml_tree(start_directory, gitignore=gitignore_file)
    else:
        tree = create_yaml_tree(start_directory)

    save_yaml(tree, output_yaml_file)

    print(f"Working tree saved to {output_yaml_file}")
