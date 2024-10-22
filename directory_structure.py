import os

def print_directory_structure(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for root, dirs, files in os.walk(root_dir):
            # Calculate the indentation level
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            # Write the directory name
            file.write(f"{indent}{os.path.basename(root)}/\n")
            # Write the file names
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                file.write(f"{sub_indent}{f}\n")

if __name__ == "__main__":
    # Get the directory where this script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Specify the output text file path (placed in the same directory)
    output_text_file = os.path.join(script_directory, "directory_structure.txt")
    
    print_directory_structure(script_directory, output_text_file)
    print(f"Directory structure of '{script_directory}' has been written to '{output_text_file}'.")
