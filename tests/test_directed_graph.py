from unittest import TestCase
from src.directed_graph import DirectedGraphHandler


class TestDirectedGraphHandler(TestCase):

    def test_parse_user_input(self):
        # valid user input, no dependencies
        input1 = "a => , b => , c => "
        result1 = DirectedGraphHandler._parse_user_input(input1)
        expected_output1 = [("a", ""), ("b", ""), ("c", "")]
        self.assertEqual(expected_output1, result1)

        # valid user input, dependency
        input2 = "a => b, b =>"
        result2 = DirectedGraphHandler._parse_user_input(input2)
        expected_output2 = [("a", "b"), ("b", "")]
        self.assertEqual(expected_output2, result2)

        # invalid user input, absence of '=>'
        input3 = "a, b =>"
        self.assertRaises(IOError,
                          DirectedGraphHandler._parse_user_input, input3)

        # invalid user input, absence of '=>'
        input4 = "a"
        self.assertRaises(IOError,
                          DirectedGraphHandler._parse_user_input, input4)

    def test_add_trailing_comma(self):
        # needs appended comma
        input1 = "a,b,c"
        result1 = DirectedGraphHandler._add_trailing_comma(input1)

        # does not need appended comma
        input2 = "a,b,c,"
        result2 = DirectedGraphHandler._add_trailing_comma(input2)

        expected_output = "a,b,c,"

        self.assertEqual(expected_output, result1)
        self.assertEqual(expected_output, result2)

    def test_build_graph(self):
        # valid graph with no dependencies
        input1 = [("a", ""), ("b", ""), ("c", "")]
        result1 = DirectedGraphHandler._build_graph(input1)
        expected_output1 = {"a": "", "b": "", "c": ""}
        self.assertEqual(expected_output1, result1)

        # valid graph with dependency
        input2 = [("a", "b"), ("b", "c"), ("c", "")]
        result2 = DirectedGraphHandler._build_graph(input2)
        expected_output2 = {"a": "b", "b": "c", "c": ""}
        self.assertEqual(expected_output2, result2)

        # duplicate jobs in list, throw IOError
        input3 = [("a", ""), ("a", "")]
        self.assertRaises(IOError,
                          DirectedGraphHandler._build_graph, input3)

        # self loop in list item, throw IOError
        input4 = [("a", "a")]
        self.assertRaises(IOError,
                          DirectedGraphHandler._build_graph, input4)

        # job depends on job which does not exist, throw IOError
        input5 = [("a", "f")]
        self.assertRaises(IOError,
                          DirectedGraphHandler._build_graph, input5)

    def test_topological_sort(self):
        handler = DirectedGraphHandler("")

        # graph with only one job, no dependencies
        handler.graph = {"a": ""}
        result1 = handler.topological_sort()
        expected_output1 = ["a"]
        self.assertEqual(expected_output1, result1)

        handler.graph.clear()

        # graph with multiple jobs, no dependencies
        handler.graph = {"a": "", "b": "", "c": ""}
        result2 = handler.topological_sort()
        expected_outputs2 = [
            ["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"],
            ["a", "c", "b"], ["c", "b", "a"], ["b", "a", "c"]
        ]
        self.assertIn(result2, expected_outputs2)

        handler.graph.clear()

        # graph with multiple jobs, one dependency
        handler.graph = {"a": "", "b": "c", "c": ""}
        result3 = handler.topological_sort()
        expected_outputs3 = [["c", "b", "a"], ["c", "a", "b"],
                             ["a", "c", "b"]]
        self.assertIn(result3, expected_outputs3)

        handler.graph.clear()

        # graph with multiple dependencies
        handler.graph = {
            "a": "b", "b": "", "c": "a", "d": "a"
        }
        result4 = handler.topological_sort()
        expected_outputs4 = [
            ["b", "a", "c", "d"],
            ["b", "a", "d", "c"]
        ]
        self.assertIn(result4, expected_outputs4)



