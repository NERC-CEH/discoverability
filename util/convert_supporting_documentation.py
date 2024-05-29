#!/usr/bin/env python

import yaml, glob, zipfile, os, justext
from tika import parser
from pathlib import Path


def convert_supporting_documentation(path):
    for zip in glob.glob(f'{path}/*.zip'):
        extract_path = zip.replace('.zip', '')
        os.makedirs(extract_path, exist_ok=True)
        #print(f'Extracting {zip}')
        with zipfile.ZipFile(zip, 'r') as zip_file:
            zip_file.extractall(zip.replace('.zip', ''))
            convert_pdfs_and_docs(extract_path)


def clean_text(text):
    paras = justext.justext(text, justext.get_stoplist('English'))
    cleaned_text = ''
    for para in paras:
        if not para.is_boilerplate:
            cleaned_text += para.text
    return cleaned_text


def convert_pdfs_and_docs(path):
    types = ['.pdf', '.doc', '.docx', '.rtf']
    files = []
    for type in types:
        files.extend(glob.glob(f'{path}/**/*{type}', recursive=True))
    for file in files:
        filename = Path(file).name
        print(f'Extracting text from {filename}')
        parsed_file = parser.from_file(file)
        cleaned_text = clean_text(parsed_file['content'])
        with open(f'{file}.txt', 'w') as f:
            f.write(cleaned_text)


if __name__ == '__main__':
    config = yaml.safe_load(open('config.yml'))
    convert_supporting_documentation(config['save_path'])

