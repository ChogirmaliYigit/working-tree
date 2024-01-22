import os
import yaml
from gitignore_parser import parse_gitignore


def create_yaml_tree(directory, ignore_list=None, level=0):
    if ignore_list is None:
        ignore_list = []

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
        if item not in ignore_list:
            path = os.path.join(directory, item)

            if os.path.isdir(path):
                # Recursively call for subdirectories
                result[item] = create_yaml_tree(path, ignore_list, level + 1)
            elif os.path.isfile(path):
                result[item] = f"{os.path.getsize(path)}B"
            else:
                result[item] = None

    return result


def save_yaml(work_tree, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(work_tree, file, default_flow_style=False)


def make_tree(start_directory='.', output_file=None):
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Use the current working directory if start_directory is not provided
    start_directory = start_directory or os.getcwd()

    if output_file is None:
        output_file = os.path.join(script_directory, 'working_tree.yaml')

    # Save the YAML tree to the output file in the specified directory
    save_yaml(create_yaml_tree(start_directory), output_file)

    print(f"Working tree saved to {output_file}")
