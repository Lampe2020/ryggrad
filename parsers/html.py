# -*- coding: utf-8 -*-

"""
ryggrad HTML parser
"""

import re, typing

class DOMTree:
    """
    The base class for all DOM elements and entire trees
    """
    doctype:str = 'html'
    doctype_props:dict[str, str] = {}
    elements:list[typing.Type[DOMTree]]

class HTMLElement(DOMTree):
    """
    Base HTML element. The parser returns this if it encounters an element that it doesn't recognize.
    """

    __selfclosing:bool = False

    def __init__(self, tagname:str, attrs:dict[str, str]={}, props:dict[str, any]={}, children:list=[typing.Self, str]):
        """
        Initializes the HTML element
        :param tagname:
        :param attrs:
        :param props:
        """
        super().__init__()
        self.tagname:str = str(tagname)
        self.attrs:dict[str, str] = {**attrs}
        self.props:dict[str, any] = {**props}
        self.__children:list[typing.Type[HTMLElement]] = [child for child in children if isinstance(child, HTMLElement)]

    def __str__(self) -> str:
        """
        Returns the raw HTML of the HTML element.
        :return:
        """
        return (f'<{self.tagname.lower()}{"" if self.__selfclosing else ">"}'
                f'{"".join(str(child) for child in self.__children)}'
                f'{"/>" if self.__selfclosing else f"</{self.tagname.lower()}>"}')

    def __repr__(self) -> str:
        """
        Returns a representation of the HTML element
        :return:
        """
        return (f'{type(self).__name__}('
                f'tagname={repr(self.tagname)}, '
                f'attrs={repr(self.attrs)}, '
                f'props={repr(self.props)}, '
                f'children={repr(self.__children)})')

    #TODO: Implement the other needed methods!

def parse(markup:str, dynamic:bool=False, scripthandler:None|typing.Callable=None) -> DOMTree:
    """
    Parses the given HTML and returns it as a `DOMTree`.
    Setting the `dynamic` argument to `False` means the markup parsing can be interrupted by scripts. In that case, a
    callable object needs to be provided to the `scripthandler`, which takes the HTMLElement decendant that caused the
    parser to kickstart script execution as the first argument (`kickstart:typing.Type[HTMLEmenent]=`) and the entire
    so-far-parsed DOM tree as the second argument (`dom:DOMTree=`).
    :param markup:
    :param static:
    :return:
    """
    if static and not scripthandler:
        raise ValueError('parsers.html.parse(): No script handler provided in non-static mode!')
    domtree:DOMTree = DOMTree()
    elmnt_stack:list[typing.Type[HTMLElement]] = [] # Elements are added to here when needed. If a script removes them
                                                    # during parsing, the stack is walked back upwards until an element
                                                    # that is still present in the DOMTree is found.
    #TODO: Implement parser logic!
    return HTMLElement(
        tagname='html-parse-error',
        attrs={'title', 'Parser not implemented yet!'},
        props={},
        children=["Please note that the HTML parser isn't implemented yet!"]
    )
