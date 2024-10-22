import os

# Specify the file extensions you want to include
file_extensions = ['.py', '.md', '.txt']

# Specify the output file where all the content will be merged
output_file = 'merged_output.txt'

def is_important_file(file):
    """Check if the file has one of the important extensions."""
    return any(file.endswith(ext) for ext in file_extensions)

def merge_files_into_one(repo_dir, output_file):
    """Walk through the directory and merge important files into one."""
    with open(output_file, 'w') as outfile:
        # Walk through the directory recursively
        for root, dirs, files in os.walk(repo_dir):
            for file in files:
                # Check if the file is important
                if is_important_file(file):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, repo_dir)
                    try:
                        # Read and append file contents to the output file
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            # Write the relative file path as a header
                            outfile.write(f"# Location of {relative_path}\n\n")
                            outfile.write(infile.read())
                            outfile.write(f"\n--- End of {relative_path} ---\n\n")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    # Specify the directory where your GitHub repo is located
    repo_dir = os.path.abspath(os.path.dirname(__file__))  # Modify this if needed
    merge_files_into_one(repo_dir, output_file)
    print(f"All important files have been merged into {output_file}")
