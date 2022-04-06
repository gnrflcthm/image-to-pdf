from PIL import Image
from pdfrw import PdfReader, PdfWriter
import os
import sys
import shutil

INPUT_DIR = "./input"
TEMP_DIR = "./temp"
OUTPUT_DIR = "./output"

def convert_to_pdf():
    input_files = [f'{INPUT_DIR}/{y}' for y in [x for x in os.walk(INPUT_DIR)][0][2]]
    for f in input_files:
        if f.split("/")[-1] == ".blank": continue
        with Image.open(f) as img:
            converted = img.convert("RGB")
            file_name = f.split("/")[-1].split(".")[0]
            converted.save(f"./{TEMP_DIR}/{file_name}.pdf")

def merge_pdf(filename):
    input_files = [f'{TEMP_DIR}/{y}' for y in [x for x in os.walk(TEMP_DIR)][0][2]]
    writer = PdfWriter(fname=f"{OUTPUT_DIR}/{filename}")
    for f in input_files:
        if f.split("/")[-1] == ".blank": continue
        pdf = PdfReader(f)
        writer.addPage(pdf.pages[0])
    writer.write()

def generate_pdf():
    filename = ""
    if len(sys.argv) == 1:
        filename = "output"
    else:
        filename = sys.argv[1]
    convert_to_pdf()
    merge_pdf(filename)
    clear_temp()

def clear_temp():
    input_files = [f'{TEMP_DIR}/{y}' for y in [x for x in os.walk(TEMP_DIR)][0][2]]
    for f in input_files:
        if f.split("/")[-1] == ".blank": continue
        os.remove(f)
    pass

generate_pdf()