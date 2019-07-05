from typing import *


class DirectedGraphHandler(object):

    def __init__(self, user_input: str):
        """
        Initialises empty directed graph, builds graph from user input string.

        :param user_input: string representation of jobs and their dependencies
        """
        self.graph = {}
        input_rows = self._parse_user_input(user_input)
        self.graph = self._build_graph(input_rows)

    def topological_sort(self) -> List[str]:
        """
        Order the instance's graph dictionary as a string into topological sort.

        :return: list of jobs from graph in topological sort
        """
        out_list = []
        start_nodes = set(key for key, value in self.graph.items() if value == "")
        aux_graph = self.graph.copy()

        # This algorithm works well for smaller examples. To optimise for larger
        # problems, our graph should contain a list of incoming nodes as well
        # as outgoing nodes and therefore the linear search through all of
        # the keys in the graph could be replaced with a loop through the
        # "outgoing" node list for "this_node"
        while start_nodes:
            this_node = start_nodes.pop()
            out_list.append(this_node)

            for key, value in aux_graph.items():
                if value == this_node:
                    aux_graph[key] = ""
                    start_nodes.add(key)

        if len(out_list) != len(self.graph.keys()):
            raise ValueError("There is no way of jobs happening in series based "
                             "on the dependencies provided.")

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
        for node in nodes:
            # catching duplicate jobs
            if node[0] in temp_graph:
                raise IOError("Job with label {} duplicated in input"
                              "\nJobs cannot have multiple dependencies.".format(node[0]))

            # catching self loops
            if node[0] == node[1]:
                raise IOError("Job with label {} cannot be dependent upon "
                              "itself".format(node[0]))

            temp_graph[node[0]] = node[1]

        keys = temp_graph.keys()
        for key, value in temp_graph.items():
            if value not in keys and value != "":
                raise IOError("Job with label {} cannot depend on Job {} "
                              "since Job {} does not exist."
                              .format(key, value, value))

        return temp_graph

    @staticmethod
    def _parse_user_input(user_input: str) -> List[tuple]:
        """
        Handles string input and converts it to list representation of jobs and
        dependencies. Deals only with syntactic errors in input string.

        :param user_input: string representation of jobs and their dependencies
        :return: list of tuples containing of the form (job, dependency)
        """
        rows = []

        for row in user_input.split(","):
            if "=>" not in row:
                raise IOError("The information entered did not follow the "
                              "program description.\n\t \"a => , b => c, "
                              "c => \".")

            key, value = row.split("=>")
            rows.append((key.strip(), value.strip()))

        return rows
