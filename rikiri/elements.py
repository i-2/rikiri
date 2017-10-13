"""elements for presentation"""

import os.path as path
from .base import Tag, ContentFrame, FileNode

class Template(Tag):  
    """Template Strings""" 
    _tag = "textarea"
    _attrs = ("template",)


class MarkSection(Tag):
    """Markdown section"""
    _tag = "section"
    _attrs = ("markdown",)


class MarkdownFrame(ContentFrame):
    """A Segemnt to hold the markdown in html"""
    _parent_tag = MarkSection
    _child_tag = Template


class MarkdownFile(FileNode):
    """Segment to hold the file"""
    _ext = ".md"
    _frame = MarkdownFrame


def get_file_node(_path):
    """Get the file node based on file extension"""
    print(_path)
    name = path.basename(_path)
    if ".md" in name:
        return MarkdownFile(name, _path)
    return
