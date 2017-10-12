"""render the file accordingly"""

import os
import shutil
import os.path as path
from jinja2 import Template
from .walk import Walker
from .base import Slides
from .elements import get_file_node

def convert_absolute(output_dir):
    if not path.isabs(output_dir):
        output_dir = path.join(os.getcwd(), output_dir)
    return output_dir

def copy_contents(output_dir):
    """copy the contents to output directory"""
    output_dir = convert_absolute(output_dir)
    shutil.copytree(path.join(path.dirname(__file__), "../contents"), output_dir)
    return None

def copy_template(output_dir, **kwargs):
    """copy the template file to output directory"""
    path_template = path.join(path.dirname(__file__), "../templates/index.jinja2")
    output_file = path.join(convert_absolute(output_dir), "index.html")
    template = Template(open(path_template).read())
    fp = open(output_file, "w")
    fp.write(template.render(**kwargs))
    fp.close()

def get_slides(source_dir):
    """walking on the source dir to gather files"""
    source_dir = convert_absolute(source_dir)
    walker = Walker(source_dir)
    slides = Slides()
    for file in walker:
        file_node = get_file_node(file)
        slides += file_node.frame
    return slides

def render(title, source_dir, target_dir):
    """renders all the necessary changes to work"""
    copy_contents(target_dir)
    slides = get_slides(source_dir)
    copy_template(target_dir, data=str(slides), title=title)