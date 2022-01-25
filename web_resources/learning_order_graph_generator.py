"""
learning_order_graph_generator.py
01/24/22
Contributors: Levi Purdy

This script is used to prepare the obsidian markdown notes for web publication.
It is intended to be run from the command line.

This file is meant to generate a complete prerequisite tree from markdown files in a learning order.
"""

"""
Probably should use this as an opportunity to learn networkx
https://networkx.org/documentation/stable/tutorial.html

Reference PDF:
https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf
"""

import glob

from subgraph_generator import *

main_graph_file_name = "Learning_Order_Graph.md"

def main():
    md_files_directory = "../notes"
    md_file_list = list_markdown_files(md_files_directory)

    for md_file in md_file_list:
        wikilinks = find_wikilinks(md_file)

if __name__ == "__main__":
    main()