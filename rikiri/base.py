""" gleam.py """

from yattag import SimpleDoc
from jinja2 import Template

DEFAULT_TEMPLATE = """
<div class="reveal">
    <div class="slides">
			{{data}}
	</div>
</div>
"""

class HTMLDoc(SimpleDoc):
    """Doc with html method"""
    def html(self, *strgs):
        for strg in strgs:
            self._append(strg)

    def taghtml(self):
        return self, self.tag, self.html


def get_doc(*args, **kwargs):
    """get the base document to be filled"""
    return HTMLDoc().taghtml()

def transform_attr(prefix):
    """Transform all attr to be named with some prefix"""
    def inner_transform(*args):
        _attrs = {}
        _args = []
        for arg in args:
            if isinstance(arg, (tuple, list)):
                key, value = arg
                _prefix_key = "{}-{}".format(prefix, key)
                _attrs[_prefix_key] = value
            else:
                attr_prop = "{}-{}".format(prefix, arg)
                _args.append(attr_prop)
        return _args, _attrs
    return inner_transform

class Tag(object):
    """Base tag for all wrappers"""

    _tag = ""
    _attrs = ()
    _defaults = {}
    _attr_prefix = "data"

    def __init__(self, content, **kwargs):
        self._content = content
        self.childs = []
        self._attrs += kwargs.get("attrs", ())

    def add_child(self, other):
        self.childs.append(other)
        return self

    def __str__(self):
        doc, tag, html = get_doc(defaults=self._defaults)
        attrs_t = transform_attr(self._attr_prefix)
        args, atts = attrs_t(*self._attrs)
        with tag(self._tag, *args, **atts):
            html(self._content)
            for child in self.childs:
                html(str(child))
        return doc.getvalue()

class Slides(object):
    """Slides of presentations"""
    def __init__(self, slides=None):
        self.slides = slides or []
  
    def add(self, other):
        self.slides.append(other)

    def __str__(self):
        template = Template(DEFAULT_TEMPLATE)
        _data = map(str, self.slides)
        return template.render(data="\n".join(_data))

class ContentFrame(object):
    """Simple frame to get the content wrap"""

    _parent_tag = None
    _parent_attrs = ()
    _child_tag = None
    _child_attrs = ()

    def __init__(self, content):
        self.content = content

    def __str__(self):
        p_tag = self._parent_tag("", attrs=self._parent_attrs)
        c_tag = self._child_tag(self.content, attrs=self._child_attrs)
        p_tag.add_child(c_tag)
        return str(p_tag)

class FileNode(object):
    """File in a folder"""
    _ext = None
    _frame = None
    
    def __init__(self, name, path):
        self.name = name
        self.path = path

    @property
    def contents(self):
        fp = open(self.path, "r")
        _contents = fp.read().decode('utf-8')
        fp.close()
        return _contents

    @property
    def frame(self):
        return self._frame(self.contents)