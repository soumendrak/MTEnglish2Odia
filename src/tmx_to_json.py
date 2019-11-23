"""
Author: Soumendra Kumar Sahoo
Usage: 
>>> python tmx_to_json.py <.xml file> <.txt output file>
"""
import json
import re
import sys
import xmltodict

from character_mapping import MATRA

cleaner = re.compile('<.*?>')

def remove_html_tags(text):
  cleantext = re.sub(cleaner, '', text)
  return cleantext

def check_odia_text(text):
    if any(matra in text for matra in MATRA):
        return True
    else:
        return False

def read_xml_file(filename):
    with open(filename, 'r+', encoding='utf-8') as fh:
        xml_file = fh.read()
    return xml_file

def process_file(xml_file):
    final_file = set()
    file_dict = xmltodict.parse(xml_file)
    for each_par in file_dict.get('tmx').get('body').get('tu'):
        en_sentence = remove_html_tags(each_par.get('tuv')[0]['seg']).strip()
        or_sentence = remove_html_tags(each_par.get('tuv')[1]['seg']).strip()
        if check_odia_text(or_sentence):
            write_sentence = en_sentence + '||' + or_sentence
            final_file.add(write_sentence)  # keep only unique pairs
    final_file = '\n'.join(final_file)
    return final_file

def write_final_file(final_file, filename=None):
    with open(filename or 'output_file.txt', 'w+', encoding='utf-8') as wh:
        wh.write(final_file)
    print('Written')

def main():
    xml_file = read_xml_file(filename=sys.argv[1])
    final_file = process_file(xml_file)
    write_final_file(final_file, sys.argv[2])

if __name__ == '__main__':
    main()