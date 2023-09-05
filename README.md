# File Deletion Script

## Overview

This Python script is designed to help you manage your files by deleting files in a specified directory that exceed a minimum size threshold. It provides an interactive interface for confirming file deletion, ensuring that you don't accidentally remove important files.

## Features

- Interactive file deletion confirmation.
- Specify the directory to search for files.
- Set a minimum file size threshold (in megabytes).
- Display file sizes in a human-readable format.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed on your system.

## Usage

1. **Clone or Download**: Clone or download the script to your local machine.

2. **Open Terminal or Command Prompt**: Open your terminal or command prompt and navigate to the directory containing the script.

3. **Run the Script**: Run the script with the following command:

```bash
python3 delete_files.py --directory <directory_path> --min-size <min_size>
```



- Replace <directory_path> with the path to the directory where you want to delete files.
- Replace <min_size> with the minimum file size in megabytes. By default, this is set to 1 megabyte.

Example:
```bash
python file_deletion_script.py --directory /path/to/your/directory --min-size 10
```

- This command will search for files larger than 10 megabytes in the specified directory and ask for confirmation before deleting each one.


1. **The script will start scanning the specified directory for files larger than the minimum size threshold.** It will display a list of files and ask for your confirmation before deleting each one. To confirm deletion, type 'y'; to skip, type 'n'.

Example:
```shell
Delete '/path/to/your/directory/large_file.txt'? (y/n): y
Deleted '/path/to/your/directory/large_file.txt'
```

2. **After the script completes, it will inform you if any deletions occurred or if the operation was unsuccessful.**
```shell
Deletion completed.
```

## Notes

- Be cautious when using this script, especially with the --min-size option, as it can permanently delete files from your system.

- If you decide to cancel the operation at any time, you can do so by pressing Ctrl + C.

# Author

* Author: Jonathan Mshelia
* Email: jonathanjamesm66@gmail.com