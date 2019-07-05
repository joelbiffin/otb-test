from typing import *


class DirectedGraphHandler(object):

    def __init__(self, user_input: str):
        """
        Initialises empty directed graph, builds graph from user input string.

        :param user_input: string representation of jobs and their dependencies
        """
        self.graph = {}

    def topological_sort(self) -> List[str]:
        """
        Order the instance's graph dictionary as a string into topological sort.

        :return: list of jobs from graph in topological sort
        """
        out_list = []
        # TODO: topologically sort directed graph
        return out_list

    @property
    def sorted_nodes(self):
        return "{}".format(str(self.topological_sort()))

    @staticmethod
    def _add_trailing_comma(string: str) -> str:
        """Appends trailing comma to string if doesn't already exist."""
        if string.rstrip().endswith(","):
            return string
        else:
            return string + ","

    @staticmethod
    def _build_graph(nodes: List[tuple]) -> dict:
        """
        Builds instance's graph hashtable from pre-parsed list of tuples. Deals
        with self-dependencies, duplicate job definitions and jobs dependent on
        those which do not exist.

        :param nodes: pre-parsed list of tuples of the form (job, dependency)
        :return: hashtable representing the graph of jobs and dependencies
        """
        temp_graph = {}
        # TODO: build graph from list of tuples
        return temp_graph

    @staticmethod
    def _parse_user_input(user_input: str) -> List[tuple]:
        """
        Handles string input and converts it to list representation of jobs and
        dependencies. Deals only with syntactic errors in input string.

        :param user_input: string representation of jobs and their dependencies
        :return: list of tuples containing of the form (job, dependency)
        """
        rows = [()]
        # TODO: turn string user input into list of tuples
        return rows
