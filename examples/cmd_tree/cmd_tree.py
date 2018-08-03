# -*- coding: utf-8 -*-
"""
A tool for generating a HTML page with a table showing which commands are available in different command trees.
Useful for seeing which commands are available on both ZNB and ZVA.

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
from collections import defaultdict

import dominate
from dominate.tags import *

import re

from RSSscpi.gen import ZVA_gen, ZNB_gen
from RSSscpi.SCPI_gen_support import SCPIQuery, SCPISet, SCPINodeBase

# dict(cmd string -> dict(vna name -> cmd object))


def cmd_tree_load(vna_name, cmd_root, commands):
    """

    :param unicode vna_name: A string identifying the command tree structure
    :param SCPINodeBase cmd_root: A (sub)-tree of a SCPINodeBase tree
    :param defaultdict commands: A defaultdict for storing the flattened commands, with default return dict()
    :return: The populated `commands` dict.
    """
    for name in cmd_root.__class__.__dict__:
        cmd = getattr(cmd_root, name)
        if isinstance(cmd, SCPINodeBase):
            if isinstance(cmd, (SCPIQuery, SCPISet)):
                cmd_string = cmd.build_cmd()
                commands[cmd_string][vna_name] = cmd
            cmd_tree_load(vna_name, cmd, commands)
    return commands


def tree_txt_out(commands, vna_list):
    fmt = "%s\t%s\t%s"
    for cmd in sorted(commands.keys()):
        x = commands[cmd]
        print(fmt % (cmd, x.get(vna_list[0]), x.get(vna_list[1])))


def tree_dominate(commands, vna_list):
    doc = dominate.document(title="VNA cmd ref")
    re_url = re.compile("<(.*)>")
    doc.head += script(src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js")
    doc.head += script(src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js")
    doc.head += link(rel="stylesheet", type="text/css", href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css")

    doc.head += script(src="https://cdn.datatables.net/fixedheader/3.1.5/js/dataTables.fixedHeader.min.js")
    doc.head += link(rel="stylesheet", type="text/css", href="https://cdn.datatables.net/fixedheader/3.1.5/css/fixedHeader.dataTables.min.css")

    doc.head += script(src="cmd_tree.js")
    doc.head += link(rel="stylesheet", type="text/css", href="cmd_tree.css")

    with doc.body:
        with table(cls="cmd-table"):
            with thead().add(tr()):
                th("Command")
                for vna in vna_list:
                    th(vna, cls="vna-col")
            with tbody():
                for cmd in sorted(commands.keys()):
                    with tr():
                        td(cmd)
                        for vna in vna_list:
                            try:
                                node = commands[cmd][vna]
                            except KeyError:
                                td("N")
                            else:
                                href = re_url.search(node.__doc__)
                                if href:
                                    td(a("Y", href=href.group(1)))
                                else:
                                    td("Y")
            with tfoot().add(tr()):
                td(input(type="text", placeholder="Filter commands"))
                for vna in vna_list:
                    td(vna)
    with open("cmd_tree.html", "wb") as f:
        f.write(doc.render())


def main():
    commands = defaultdict(dict)
    cmd_tree_load("zva", ZVA_gen(None), commands)
    cmd_tree_load("znb", ZNB_gen(None), commands)
    # tree_txt_out(commands, ["znb", "zva"])
    tree_dominate(commands, ["znb", "zva"])


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)
    main()
