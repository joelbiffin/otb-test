from typing import *


class DirectedGraphHandler(object):

    def __init__(self, user_input: str):
        """Initialises empty directed graph,
        builds graph from user input string"""
        self.graph = {}

    def topological_sort(self) -> List[str]:
        out_list = []
        # TODO: topologically sort directed graph
        return out_list

    @property
    def sorted_nodes(self):
        return "{}".format(str(self.topological_sort()))

    @staticmethod
    def _add_trailing_comma(string: str) -> str:
        if string.rstrip().endswith(","):
            return string
        else:
            return string + ","

    @staticmethod
    def _parse_user_input(user_input: str) -> List[tuple]:
        rows = [()]
        # TODO: turn string user input into list of tuples
        return rows

    @staticmethod
    def _build_graph(nodes: List[tuple]) -> dict:
        temp_graph = {}
        # TODO: build graph from list of tuples
        return temp_graph
