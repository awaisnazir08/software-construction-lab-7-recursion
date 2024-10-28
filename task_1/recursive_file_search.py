import os
import argparse

def search_files(directory, file_names, case_sensitive=True, results=None):
    """
    Recursively search for specified files in a directory and its subdirectories.

    Args:
        directory (str): Path to the directory to search.
        file_names (list): List of file names to search for.
        case_sensitive (bool): If True, the search is case-sensitive.
        results (dict): Stores the results (file name and count of occurrences).

    Returns:
        dict: A dictionary containing each file name and a list of full paths where it was found.
    """
    if results is None:
        results = {name: [] for name in file_names}

    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                for name in file_names:
                    match = (entry.name == name) if case_sensitive else (entry.name.lower() == name.lower())
                    if match:
                        results[name].append(entry.path)
            elif entry.is_dir():
                search_files(entry.path, file_names, case_sensitive, results)
    except PermissionError:
        print(f"Permission denied: {directory}")
    except Exception as e:
        print(f"Error accessing {directory}: {e}")

    return results

def main():
    parser = argparse.ArgumentParser(description="Recursive file search program.")
    parser.add_argument("directory", type=str, help="Directory path to search within.")
    parser.add_argument("file_names", nargs='+', help="Names of files to search for.")
    parser.add_argument("--case-insensitive", action="store_true", 
                        help="Perform a case-insensitive search.")
    args = parser.parse_args()

    directory = args.directory
    file_names = args.file_names
    case_sensitive = not args.case_insensitive

    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    results = search_files(directory, file_names, case_sensitive)

    found_any = False
    for name, paths in results.items():
        if paths:
            found_any = True
            print(f"File '{name}' found {len(paths)} time(s):")
            for path in paths:
                print(f" - {path}")
        else:
            print(f"File '{name}' not found.")

    if not found_any:
        print("No files found.")

if __name__ == "__main__":
    main()
