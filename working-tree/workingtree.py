import os
import yaml
from gitignore_parser import parse_gitignore

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))
OUTPUT_YAML_FILE = os.path.join(script_directory, 'working_tree.yaml')

TREE_IGNORE = ['.git', os.path.basename(__file__), OUTPUT_YAML_FILE]


def create_yaml_tree(directory, level=0):
    result = {}

    # Get the list of items in the directory
    items = os.listdir(directory)

    # Check if there is a .gitignore file in the directory
    gitignore_file = os.path.join(directory, '.gitignore')
    if os.path.isfile(gitignore_file):
        gitignore_parser = parse_gitignore(gitignore_file)
        # Filter out items listed in .gitignore
        items = [item for item in items if not gitignore_parser(item)]

    for item in items:
        # Exclude hidden files and directories (starting with dot)
        if item not in TREE_IGNORE:
            path = os.path.join(directory, item)

            if os.path.isdir(path):
                # Recursively call for subdirectories
                result[item] = create_yaml_tree(path, level + 1)
            elif os.path.isfile(path):
                result[item] = f"{os.path.getsize(path)}B"
            else:
                result[item] = None

    return result


def save_yaml(work_tree, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(work_tree, file, default_flow_style=False)


def make_tree(start_directory='.'):
    # Save the YAML tree to the output file in the script directory
    save_yaml(create_yaml_tree(start_directory), OUTPUT_YAML_FILE)

    print(f"Working tree saved to {OUTPUT_YAML_FILE}")
