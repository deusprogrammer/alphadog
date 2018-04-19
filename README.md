# What do they do?

## Alphadog

Alphadog is for organizing a directory into folders based on their filename or extension.  You can organize either alphabetically or by file extension.  You can also re-expand a directory back into a flat directory using the --expand option.
You can also set other options like the maximum number of files per directory with the --max_files option.  You can also use options to put your organized files into a different folder using the --target option and even have it delete the original directory using the --move options.

### Examples:

#### Sort C:\folder_to_be_sorted alphabetically and move to C:\another_folder with a maximum of 1024 files per folder (other files will be placed in numbered alphabetical folders i.e. A(1), A(2), etc)

	alphadog.py --sort ALPHA --target C:\another_folder --move --max_files 1024 C:\folder_to_be_sorted

### Usage

	alphadog.py [-h] [--sort {ALPHA,EXTENSION}] [--expand] [--target TARGET] [--move] [--max_files MAX_FILES] directory

## Deepthroat

Deepthroat is a filtering script that will aid in filtering files from one directory to another using regex patterns.  Regex is not trivial to understand so I will leave figuring out regex patterns to the user of the script.

### Examples:
	
#### Filter files in C:\folder_to_be_filtered that have "Mario" in the filename and put them in C:\another_folder
	deepthroat.py --target C:\another_folder --regex "^.*Mario.*$" C:\folder_to_be_filtered

### Usage

	deepthroat.py [-h] [--target TARGET] [--regex REGEX] directory
