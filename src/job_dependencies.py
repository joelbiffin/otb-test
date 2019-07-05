from directed_graph import DirectedGraphHandler


def process_user_input(user_input: str):
    try:
        graph_handler = DirectedGraphHandler(user_input)

    except IOError as error:
        print(error)
        print("Please re-run the program with the correct input "
              "formatting (above)")

    except ValueError as error:
        print(error)
        print("Please re-run the program with a job list which"
              " can be executed in series")

    else:
        print(graph_handler.sorted_nodes)


process_user_input(input("Please enter the job dependency"
                         " list in the form, a => , b => a (no quotes):\t"))
