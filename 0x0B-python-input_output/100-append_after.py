#!/usr/bin/python3
""" Appendin tl file line method """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after
    each line containing a specific string
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines += [line]
            if line.find(search_string) != -1:
                lines += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(lines))

