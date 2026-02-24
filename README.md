# Files Organizer 📂

Simple and safe-ish command-line tool to organize files in a directory by their file extensions.

Files are moved into folders like `pdf_container`, `jpg_container`, `zip_container`, etc.  
Folder directories are grouped into a `folder_container`.

---

## ✨ Features

- Organizes files by extension
- Groups directories separately
- Safe **dry-run mode** (no changes made)
- Automatic duplicate file resolution
- Verbose logging option
- Cross-platform (Linux, macOS, Windows)
- Installable as a global CLI tool

---

## 📦 Installation

### Install using pip

pip install files-organizer

Verify installation:

organize --help

---
### Install from GitHub (latest version)

git clone https://github.com/bigtimer-dev/Files-Organizer.git  
cd Files-Organizer  
pip install .

---

### Install from GitHub (development mode)

git clone https://github.com/bigtimer-dev/Files-Organizer.git  
cd Files-Organizer  
pip install -e .

---

## Usage

Basic usage:

organize PATH

Example:

organize ~/Downloads

---

## Dry Run (recommended)

Preview what will happen without moving files:

organize ~/Downloads --dry-run

---

## Verbose Mode

Show detailed logs:

organize ~/Downloads --verbose

---

## Command Options

- PATH — Directory to organize  
- --dry-run — Show actions without making changes  
- --verbose — Print detailed execution logs  
- --help — Show help message  

---

## How Files Are Organized

- `.pdf` → `pdf_container/`
- `.jpg` → `jpg_container/`
- `.png` → `png_container/`
- `.zip` → `zip_container/`
- No extension → `no_extension_container/`
- Directories → `folder_container/`

---

## Duplicate Files

If a file already exists in the destination folder, it is renamed automatically:

file.pdf  
file(1).pdf  
file(2).pdf  

Files are never overwritten.

---

## Notes

- Existing `_container` folders are skipped
- Designed for single-directory (non-recursive) use
- Always use `--dry-run` before running on important folders

---

## Development

git clone https://github.com/bigtimer-dev/Files-Organizer.git  
cd Files-Organizer  
pip install -e .

---

## License

MIT License © bigtimer-dev (Alvin Noboa)

