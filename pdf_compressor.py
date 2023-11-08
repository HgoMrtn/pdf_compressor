'''
This script compresses all PDF files in a given folder and its subfolders.
'''

import time, os, shutil
from termcolor import cprint
import argparse
import subprocess
import os.path
import sys
from shutil import copyfile


## Copy a file
# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy2(src, dst)

## Explore a folder and all its subfolders
# for root, dirs, files in os.walk(folder_to_scan):
#     for name in files:
#         if name.endswith((".jpg")) and "$" not in name:
#             print(name)

def compress(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: input file is not a PDF")
        sys.exit(1)

    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[power]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done.")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file')
    parser.add_argument('-c', '--compress', type=int, help='Compression level from 0 to 4')
    parser.add_argument('-b', '--backup', action='store_true', help="Backup the old PDF file")
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after compression')
    args = parser.parse_args()

    # In case no compression level is specified, default is 2 '/ printer'
    if not args.compress:
        args.compress = 2
    # In case no output file is specified, store in temp file
    if not args.out:
        args.out = 'temp.pdf'

    # Run
    compress(args.input, args.out, power=args.compress)

    # In case no output file is specified, erase original file
    if args.out == 'temp.pdf':
        if args.backup:
            copyfile(args.input, args.input.replace(".pdf", "_BACKUP.pdf"))
        copyfile(args.out, args.input)
        os.remove(args.out)

    # In case we want to open the file after compression
    if args.open:
        if args.out == 'temp.pdf' and args.backup:
            subprocess.call(['open', args.input])
        else:
            subprocess.call(['open', args.out])

# if __name__ == '__main__':
#     main()



## BEGINNING OF THE SCRIPT
print(" ")
folder_to_scan = input("Type the path to the folder to scan, then hit Enter : ")
temporary_folder = input("Type the path to the safety folder, then hit Enter : ")

folder_to_scan = "/Users/hugo/Desktop/files/" # Bypass the input for testing purposes
temporary_folder = "/Users/hugo/Desktop/saving/" # Bypass the input for testing purposes

# Explore a folder and all its subfolders
pdf_names = []
for root, dirs, files in os.walk(folder_to_scan):
    for name in files:
        if name.endswith((".pdf")) and "$" not in name:
            pdf_names.append(name)
            # print(name)

# Create a list of the pdf files with their path
pdf_files = []
for path, subdirs, files in os.walk("/Users/hugo/Desktop/files/"):
    for name in files:
        if name.endswith((".pdf")) and "$" not in name:
            pdf_files.append(os.path.join(path, name))

nbr_files = len(pdf_files)
print(f"{nbr_files} files were found.")
print(f"FILES TO CONVERT: {pdf_files}")

for current_pdf in range(nbr_files):
    print(" ")
    pdf_to_compress = pdf_files[current_pdf] # Path to the file to compress
    new_destination = temporary_folder + pdf_names[current_pdf] # Path to the safety folder with the file name
    shutil.move(pdf_to_compress, new_destination) # Move the pdf to compress to the safety folder
    time.sleep(2)
    compress(new_destination, pdf_to_compress, 2) # Compress the pdf and save it to its original folder, leaving the original one in the safety folder

print(" ")
print("--- JOB DONE ---")
print(" ")
