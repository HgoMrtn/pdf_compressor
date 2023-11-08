# PDF Compressor

This Python script is designed to compress all PDF files within a specified folder and its subfolders. The script utilizes Ghostscript, a command-line tool for manipulating PDF documents. It provides a convenient way to reduce the file size of PDFs while preserving their quality.

## How It Works
The script first prompts the user to input the path to the folder containing the PDF files to be compressed. It also asks for the path to a temporary safety folder where the original PDF files will be moved during the compression process. 

The script then explores the specified folder and its subfolders, identifying all PDF files. Each PDF file is moved to the safety folder, compressed using Ghostscript with a specified compression level (default level is 2, which corresponds to '/printer'), and saved back to its original location. Optionally, the script can backup the original PDF files and open the compressed PDFs after the compression process.

## Prerequisites
- Python installed on your system
- Ghostscript installed (required for PDF compression)

## Usage Instructions
1. **Clone the Repository:**

```bash
git clone https://github.com/username/repository.git
cd repository
```

2. **Run the Script:**

```bash
python pdf_compressor.py
```

Follow the prompts to input the folder path and safety folder path. The script will compress all PDF files in the specified folder and its subfolders.

## Additional Notes
- Ensure Ghostscript is properly installed on your system. You can download it from the official Ghostscript website: [https://www.ghostscript.com/](https://www.ghostscript.com/)
- Use the script responsibly and only on PDF files you have the right to modify and compress.

Feel free to contribute and enhance the script's functionality.

