from typing import List
import argparse
import re
from colorama import Fore, Back, Style

from parsers.bibliography_parser import BibliographyParser
from parsers.citation_parser import CitationParser
from parsers.examples_parser import ExamplesParser


def load(file):
    data: List[str] = []

    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            data.append(line)

    return data


PATTERNS = {
    'bib_start': [
        'References',
        'references',
        'Bibliography',
        'bibliography'
    ],
    'bib_end': [
        'Appendix',
        'appendix',
        'Appendices',
        'appendices'
    ]
}


def main():
    parser = argparse.ArgumentParser(description="Process a plain text file into LaTeX.")
    parser.add_argument('file', metavar='f', nargs='+')
    # parser.add_argument('bib', metavar='b', nargs='#')

    args = parser.parse_args()
    data = load(args.file[0])

    print_title()

    print("")
    print("[1]:  " + Fore.RED + "Searching for start of bibliography block..." + Style.RESET_ALL)

    bibliography = get_bibliography(data)
    
    print("[4]:  " + Fore.RED + f"Found {len(bibliography)} candidate bibliography entries." + Style.RESET_ALL)
    print("")
    print("Here's what I found: ")
    print("-" * 39)
    for item in bibliography:
        print(item)

    # text_data = load(args.file[0])
    # bib_data = load(args.bib[0])


def get_bibliography(data):
    length = len(data)

    for line in data:
        for pattern in PATTERNS['bib_start']:
            match = re.search(pattern, line)
            
            if match:
                group = match.group()
                group_str = f"match '{group}' "
                span_str = f"[span {match.span()[0]}-{match.span()[1]}] "
                start_index = data.index(line)
                index_str = f"at index {start_index}"
                print("[2]:  " + "Found " + group_str + span_str + index_str)

    for i in range(start_index, len(data)):
        for pattern in PATTERNS['bib_end']:
            match = re.search(pattern, data[i])
            if match:
                group = match.group()
                end_index = data.index(data[i])
                print("[3]:  " + f"Found end of bibliography block at index {end_index-1}")

    bibliography = []
    for i in range(start_index+1, end_index):
        if data[i] != '':
            bibliography.append(data[i])

    return bibliography


def handle_bibliography(data):
    bibliography = BibliographyParser(data)
    return bibliography


def handle_citations(data):
    citations = CitationParser(data)
    return citations


def handle_examples(data):
    examples = ExamplesParser(data)
    return examples


def print_title():
    print("""
    ---------------------------------------
    |           PyTxtBib  v.1.0           |
    |   A LaTeX/BibTeX Parser in Python   |
    |                                     |
    |            Jonathan Crum            |
    |        University of Georgia        |
    ---------------------------------------
    """)


if __name__ == '__main__':
    main()
