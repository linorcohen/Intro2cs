from ex11 import *
import test_ex11_3


def test_1():
    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    assert diagnoser.diagnose([""]) == "healthy"
    assert diagnoser.diagnose([]) == "healthy"
    assert diagnoser.diagnose(["cough", "fever"]) == "influenza"


def test_2():
    healthy_leaf = Node("healthy", None, None)
    cold_leaf1 = Node('cold', None, None)
    inner_path1 = Node('headache', cold_leaf1, healthy_leaf)
    cold_leaf2 = Node('cold', None, None)
    covid_leaf = Node('covid-19', None, None)
    inner_path2 = Node('headache', covid_leaf, cold_leaf2)
    root2 = Node('cough', inner_path2, inner_path1)

    diagnoser2 = Diagnoser(root2)

    assert diagnoser2.all_illnesses() == ['cold', 'covid-19', 'healthy']


def test_3():
    records1 = parse_data('test_all_illness1.txt')
    symptoms1 = ['a', 'b']
    diagnoser_root1 = build_tree(records1, symptoms1)
    # print_tree(diagnoser_root1.root)

    records2 = parse_data('test_all_illness2.txt')
    symptoms2 = ['a', 'b', 'c', 'd', 'e']
    diagnoser_root2 = build_tree(records2, symptoms2)
    # print_tree(diagnoser_root2.root)

    symptoms2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n']


def test_4():
    symptoms = []
    records = parse_data("test_all_illnesses.txt")
    for record in records:
        for symptom in record.symptoms:
            if symptom not in symptoms:
                symptoms.append(symptom)
    assert build_tree(records, symptoms).all_illnesses() == ["influenza",
                                                             "cold", "strep",
                                                             "mono",
                                                             "healthy"], f"""the output from the function all_illnesses should not be:\n{build_tree(records, symptoms).all_illnesses()}\nbut: ["influenza", "cold", "strep", "mono", "healthy"]\nthe diagnoser was built by the function built_tree with the records taken from test_all_illnesses.txt"""


def test_5():
    records1 = parse_data('test_all_illness1.txt')
    symptoms1 = []
    diagnoser_root1 = build_tree(records1, symptoms1)
    print(diagnoser_root1.all_illnesses())


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.negative_child, level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.positive_child, level + 1)


def check_exception():
    for combo in itertools.combinations(['a', 'b', 'b'], 2):
        return combo


def test_6():
    record1 = Record('b', [])
    record2 = Record('a', ['5'])
    print(build_tree([record1, record2], ['3', '5']))


def print_in_order(diagno: Diagnoser):
    printable = ['']

    def print_in_order_helper(cur_node: Node):
        if cur_node is None:
            return
        if cur_node.positive_child:
            print_in_order_helper(cur_node.positive_child)
        printable[0] += str(cur_node.data) + ' '
        if cur_node.negative_child:
            print_in_order_helper(cur_node.negative_child)

    print_in_order_helper(diagno.root)
    return printable[0][:-1]


def test_7():
    diagnoser7 = Diagnoser(Node("cough", Node(None), Node(None)))
    diagnoser7.minimize()
    assert print_in_order(diagnoser7) == "None"

    flu_leaf8 = Node("influenza", None, None)
    none_leaf8 = Node(None, None, None)
    healthy_leaf8 = Node("healthy", None, None)
    inner_vertex7 = Node("headache", flu_leaf8, flu_leaf8)
    inner_vertex8 = Node("headache", healthy_leaf8, none_leaf8)
    root8 = Node("cough", inner_vertex8, inner_vertex7)

    diagnoser8 = Diagnoser(root8)
    diagnoser8.minimize()
    assert print_in_order(
        diagnoser8) == "healthy headache None cough influenza"

    none_leaf9 = Node(None, None, None)
    healthy_leaf9 = Node("healthy", None, None)
    inner_vertex9 = Node("headache", none_leaf9, none_leaf9)
    inner_vertex10 = Node("headache", healthy_leaf9, none_leaf9)
    root9 = Node("cough", inner_vertex10, inner_vertex9)
    diagnoser9 = Diagnoser(root9)
    diagnoser9.minimize()
    assert print_in_order(diagnoser9) == "healthy headache None cough None"

    flu_leaf10 = Node("influenza", None, None)
    cold_leaf10 = Node("cold", None, None)
    healthy_leaf10 = Node("influenza", None, None)
    inner_vertex11 = Node("headache", flu_leaf10, cold_leaf10)
    inner_vertex12 = Node("headache", flu_leaf10, cold_leaf10)
    root10 = Node("cough", inner_vertex11, inner_vertex12)
    diagnoser10 = Diagnoser(root10)
    diagnoser10.minimize()
    assert print_in_order(diagnoser10) == "influenza headache cold"

    flu_leaf11 = Node("influenza", None, None)
    cold_leaf11 = Node("cold", None, None)
    healthy_leaf11 = Node("influenza", None, None)
    inner_vertex13 = Node("fever", flu_leaf10, cold_leaf10)
    inner_vertex14 = Node("headache", flu_leaf10, cold_leaf10)
    root11 = Node("cough", inner_vertex13, inner_vertex14)

    diagnoser11 = Diagnoser(root11)
    diagnoser11.minimize()
    assert print_in_order(
        diagnoser11) == "influenza fever cold cough influenza headache cold"

    diagnoser7.minimize(True)
    assert print_in_order(diagnoser7) == "None"
    diagnoser8.minimize(True)
    assert print_in_order(diagnoser8) == "healthy cough influenza"
    diagnoser9.minimize(True)
    assert print_in_order(diagnoser9) == "healthy"
    diagnoser10.minimize(True)
    assert print_in_order(diagnoser10) == "influenza headache cold"
    diagnoser11.minimize(True)
    assert print_in_order(
        diagnoser11) == "influenza fever cold cough influenza headache cold"


def test_8():
    records = parse_data('tiny_data.txt')
    diagnoser = optimal_tree(records,
                             ['cough', 'fatigue', 'headache', 'nausea',
                              'fever', 'irritability', 'rigidity',
                              'sore_throat'], 2)
    print(diagnoser.calculate_success_rate(records))
    print(diagnoser.calculate_success_rate(records))
    diagnoser.minimize(True)
    print(diagnoser.calculate_success_rate(records))


def test_9():
    flu_leaf10 = Node("influenza", None, None)
    cold_leaf10 = Node("cold", None, None)
    healthy_leaf10 = Node("influenza", None, None)
    inner_vertex11 = Node("headache", flu_leaf10, cold_leaf10)
    inner_vertex12 = Node("headache", cold_leaf10, flu_leaf10)
    root10 = Node("cough", inner_vertex11, inner_vertex12)
    diagnoser10 = Diagnoser(root10)
    diagnoser10.minimize()


def test_10():
    files = ["tiny_data.txt"]
    for i in files:
        print(i)
        symps = []
        r = parse_data(i)
        for record in r:
            for s in record.symptoms:
                if s not in symps:
                    symps.append(s)
        diagnoser = optimal_tree(r, list(symps), len(symps) - 1)
        diagnoser.minimize(True)


def test_11():
    none_leaf9 = Node(None, None, None)
    healthy_leaf9 = Node("healthy", None, None)
    inner_vertex9 = Node("headache", none_leaf9, none_leaf9)
    inner_vertex10 = Node("headache", healthy_leaf9, none_leaf9)
    root9 = Node("cough", inner_vertex10, inner_vertex9)

    diagnoser9 = Diagnoser(root9)
    diagnoser9.minimize(True)



def test_13():
    # if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

    # Add more tests for sections 2-7 here.
    record1 = Record('cold', ['cough'])
    record2 = Record('influenza', ['fever', 'cough'])
    record3 = Record('healthy', [])
    records1 = [record1, record2, record3]

    assert diagnoser.calculate_success_rate(records1) == 1

    record4 = Record('covid', ['fever', 'headache'])
    records2 = records1
    records2.append(record4)
    assert diagnoser.calculate_success_rate(records2) == 3 / 4

    assert diagnoser.all_illnesses() == ['influenza', 'cold', 'healthy']

    healthy_leaf = Node("healthy", None, None)
    cold_leaf1 = Node('cold', None, None)
    path1 = Node('headache', cold_leaf1, healthy_leaf)
    cold_leaf2 = Node('cold', None, None)
    covid_leaf = Node('covid-19', None, None)
    path2 = Node('headache', covid_leaf, cold_leaf2)
    root2 = Node('cough', path2, path1)

    diagnoser2 = Diagnoser(root2)

    assert diagnoser2.all_illnesses() == ['cold', 'covid-19', 'healthy']

    assert diagnoser2.paths_to_illness("cold") == [[True, False],
                                                   [False, True]]
    assert diagnoser2.paths_to_illness("healthy") == [[False, False]]
    assert diagnoser2.paths_to_illness("covid-19") == [[True, True]]

    assert diagnoser.paths_to_illness("influenza") == [[True, True]]
    assert diagnoser.paths_to_illness("cold") == [[True, False]]
    assert diagnoser.paths_to_illness("healthy") == [[False]]
    assert diagnoser.paths_to_illness("covid-19") == []
    assert diagnoser.paths_to_illness(None) == []

    cold_leaf3 = Node('cold', None, None)
    none_leaf = Node(None, None, None)
    root3 = Node('cough', cold_leaf3, none_leaf)

    diagnoser3 = Diagnoser(root3)

    assert diagnoser3.paths_to_illness(None) == [[False]]

    records_tiny = parse_data('tiny_data.txt')
    symptoms_lst1 = ['cough', 'headache', 'fever']
    assert build_tree(records_tiny, symptoms_lst1).all_illnesses() == [
        'influenza', 'meningitis', 'mono', 'strep', 'healthy']

    record1 = Record("influenza", ["cough", "fever"])
    record2 = Record("cold", ["cough"])
    records = [record1, record2]

    assert build_tree(records, ['fever']).all_illnesses() == ['influenza',
                                                              'cold']
    assert optimal_tree(records, ['cough', 'fever'], 1).all_illnesses() == [
        'influenza', 'cold']
    assert optimal_tree(records, ['cough', 'fever'], 0).all_illnesses() == [
        'influenza']

    symptoms = ['cough', 'fatigue', 'headache', 'nausea', 'fever',
                'irritability', 'rigidity', 'sore_throat']
    root = parse_data("tiny_data.txt")
    diagnoser = optimal_tree(root, list(symptoms), len(symptoms) - 1)
    diagnoser.minimize(True)
    assert sorted(diagnoser.all_illnesses()) == sorted(
        ['influenza', 'meningitis', 'healthy', 'mono', 'cold', 'strep'])


if __name__ == '__main__':
    # test_ex11_3.test_7()
    test_10()
    # pass
