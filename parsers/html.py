"""
ryggrad HTML parser
"""

import typing

class HTMLElement:
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

def parse(markup:str) -> typing.Type[HTMLElement]:
    """
    Parses the given HTML and returns it as a tree of HTML element objects.
    :param markup:
    :return:
    """
    #TODO: Implement parser logic!
    return HTMLElement(
        tagname='html-parse-error',
        attrs={'title', 'Parser not implemented yet!'},
        props={},
        children=["Please note that the HTML parser isn't implemented yet!"]
    )