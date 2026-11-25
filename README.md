# space-freer

Interactively delete files above a size threshold to free up disk space.

## What it is

A small Python command-line tool that walks a directory, finds files larger than a minimum size, and asks for y/n confirmation before deleting each one. File sizes are shown in a human-readable format.

## Stack

- Python 3, standard library only (`os`, `argparse`, `enum`)
- `delete_files.py`: the CLI entry point
- `ByteConverter.py`: byte, KB, MB and GB helpers and a human-readable size formatter
- `ByteConverterTest.py`: a print-only demo of the converter

## Run it

Requires [Python 3](https://www.python.org/downloads/). There is nothing to install.

```bash
python3 delete_files.py --directory <directory_path> --min-size <min_size>
```

- `--directory`: path to the directory to scan (required).
- `--min-size`: minimum file size in megabytes. Defaults to 1.

Example:

```bash
python3 delete_files.py --directory /path/to/your/directory --min-size 10
```

This scans for files larger than 10 megabytes and prompts for each one. Type `y` to delete or `n` to skip:

```
Delete '/path/to/your/directory/large_file.txt'? (y/n): y
Deleted '/path/to/your/directory/large_file.txt'
```

When the scan finishes, the script reports whether any deletions occurred. Press Ctrl+C at any time to cancel.

## Safety

Deletion is permanent. Files are removed with `os.remove`, not moved to the trash, and there is no dry-run mode. Review each prompt carefully, especially with a low `--min-size`.

## License

MIT. See [LICENSE](LICENSE).

## Author

Jonathan James ([jona62](https://github.com/jona62))
