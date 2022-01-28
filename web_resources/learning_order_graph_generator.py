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
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

from subgraph_generator import *

main_graph_file_name = "Learning_Order_Graph.md"

banned_nodes = ["README", "'base_topic_format'", "Some_More_Resources_To_Use"]


def test_if_file_has_prereqs(md_file):
    """
    Returns true if the md_file has a wikilink to another file
    """
    wikilinks = find_wikilinks(md_file)
    if len(wikilinks) > 0:
        return True
    else:
        return False


def gen_mermaid_line(graph, node):
    print(node)
    successors = graph.successors(node)
    mermaid_line_string = ''
    for successor in successors:
        mermaid_line_string += node + encapsulate_name(make_markdown_filename_readable(node)) + line_string + \
                              successor + encapsulate_name(make_markdown_filename_readable(successor)) + "\n"

    return mermaid_line_string


def gen_mermaid_click_lines(nodes):
    mermaid_click_string = ''
    for node in nodes:
        mermaid_click_string += "click " + node + ' \"../' + node + '\" \"' +\
                                make_markdown_filename_readable(node) + '\"' + "\n"

    return mermaid_click_string


def gen_decending_mermaid_graph_from_digraph(graph):
    """
    Generates a top down graph from a digraph.

    in_degree is how many prereqs a node has.
    out_degree is how many nodes require this node.
    :param graph:
    :return:
    """
    line_string = '-->'

    # add graph header
    graph_text = "```mermaid\ngraph LR\n"

    # you can probably use the node name as the id in mermaid, so an iterator isn't needed.
    if not graph.is_directed():
        raise Exception("Graph is not directed")

    graph_cycles = nx.algorithms.simple_cycles(graph)
    graph_cycles_list = list(graph_cycles)
    if len(graph_cycles_list) > 0:
        print("Graph has cycles, please fix")
        print('Cycles = ' + str(graph_cycles))
        raise Exception("Graph has cycles")

    # layout initial nodes
    initial_nodes = [node for node in graph.nodes() if graph.in_degree(node) == 0]
    graph_generations = nx.algorithms.topological_generations(graph)
    graph_topological_sorted = nx.algorithms.topological_sort(graph)

    for node in graph_topological_sorted:
        node_string = gen_mermaid_line(graph, node)
        graph_text += node_string

    # have to execute it twice because the iterator need to be reset
    graph_topological_sorted = nx.algorithms.topological_sort(graph)
    graph_text += gen_mermaid_click_lines(graph_topological_sorted)

    graph_text += "```\n\n"

    return graph_text


def insert_graph_text(graph_text, md_file):
    """
    Inserts the graph text into the md_file
    """
    with open(md_file, 'w') as f:
        f.writelines(graph_text)


def main():
    md_files_directory = "../notes"
    md_file_list = list_markdown_files(md_files_directory)
    graph = nx.DiGraph()

    for md_file in md_file_list:
        wikilinks = find_wikilinks(md_file)
        for wikilink in wikilinks:
            if wikilink not in banned_nodes:
                graph.add_edge(wikilink, gen_expected_filename(md_file))

    graph_text = gen_decending_mermaid_graph_from_digraph(graph)

    insert_graph_text(graph_text, md_files_directory+"/"+main_graph_file_name)

    #print(graph.edges())
    #nx.draw(graph, with_labels=True)
    #plt.show()

if __name__ == "__main__":
    main()