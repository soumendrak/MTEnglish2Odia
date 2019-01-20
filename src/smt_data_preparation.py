# -*- coding: utf-8 -*-
"""
Prepare parallel corpora for SMT (Statistical Machine Translation)
@author: Soumendra kumar sahoo
date: 20-Jan-2019
"""
import csv
import os
import sys


class prepareCorpus:
    """
    Generate Parallel corpus from the combined file
    """

    def __init__(self, filename, delimiter=None):
        self.filename = filename
        self.delimiter = delimiter

    def read_file(self):
        """
        Possible input file extensions:
            1. csv
            2. txt
            3. xlsx
        """
        file, ext = os.path.splitext(self.filename)
        with open(self.filename, 'r') as cf:
            if ext.lower() == '.csv':
                file_data = csv.reader(cf, delimiter=self.delimiter or '||')
            elif ext.lower() == '.xlsx':
                pass
            elif ext.lower() == '.txt':
                pass
            else:
                msg = 'Invalid file extension passed'
            
        return file_data

    def prepare_english_senetnces(self, filename):
        pass

    def prepare_odia_senetnces(self, filename):
        pass


if __name__ == '__main__':
    _, filename, delimiter = sys.args
