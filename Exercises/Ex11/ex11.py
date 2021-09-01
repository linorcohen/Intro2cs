#################################################################
# FILE : ex11.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex11 2021
# DESCRIPTION: A simple program of illness diagnose with binary search tree.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import itertools


class Node:
    """
    The class Node.
    """
    def __init__(self, data, positive_child=None, negative_child=None):
        """
        A constructor for a Node object.
        :param data: Non-leaf node - The question asked at this node.
        Leaf node - The decision, , or None if there is no decision.
        :type data: str or None
        :param positive_child: Non-leaf node - The node that matches a positive
        answer to the question. Leaf node – None.
        :type positive_child: Node or None
        :param negative_child: Non-leaf node - The node that matches a negative
        answer to the question. Leaf node - None.
        :type negative_child: Node or None
        """
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    """
    The class Record.
    """
    def __init__(self, illness, symptoms):
        """
        A constructor for Record object.
        :param illness: name of illness
        :type illness: str
        :param symptoms: list of illness symptoms
        :type symptoms: list[str]
        """
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """
    This function gets a path to a file of illnesses and their symptoms,
    and returns a list of Records objects for each illness.
    :param filepath: path to file
    :type filepath: str
    :return: list of Records objects
    :rtype: List[Record]
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """
    The class Diagnoser.
    """
    def __init__(self, root):
        """
        A constructor for Diagnoser object.
        :param root: root of a tree
        :type root: Node
        """
        self.root = root

    def diagnose(self, symptoms):
        """
        This function receives a list of symptoms and "diagnoses" which disease
        matches them according to the decision tree.
        :param symptoms: list of symptoms
        :type symptoms: list[str]
        :return: illness matches the symptoms
        :rtype: str
        """
        return self.__diagnose_helper(self.root, symptoms)

    def __diagnose_helper(self, node, symptoms):
        """
        Helper function for the function diagnose():
        This function finds in a recursive way the illness that matches the
        symptoms.
        :param node: current node
        :type node: Node
        :param symptoms: list of symptoms
        :type symptoms: list[str]
        :return: node data (illness leaf)
        :rtype: str
        """
        if node.negative_child is None and node.positive_child is None:
            return node.data

        if node.data in symptoms:
            return self.__diagnose_helper(node.positive_child, symptoms)
        return self.__diagnose_helper(node.negative_child, symptoms)

    def calculate_success_rate(self, records):
        """
        This function calculates the ratio between the number of successes to
        diagnose records from records and the number of records in total.
        :param records: list of record objects
        :type records: list[Record]
        :return: success rate
        :rtype: float
        """
        if len(records) == 0:
            raise ValueError("records list can't be empty")

        successful_diagnoses = 0
        for record in records:
            if record.illness == self.diagnose(record.symptoms):
                successful_diagnoses += 1

        return successful_diagnoses / len(records)

    def all_illnesses(self):
        """
        This function returns a list of all the tree illnesses.
        :return: list of all the illnesses
        :rtype: List[str]
        """
        illnesses_dict = {}
        self.__all_illnesses_helper(self.root, illnesses_dict)
        return self.__transfer_dict_to_sorted_list(illnesses_dict)

    def __all_illnesses_helper(self, node, illnesses_dict):
        """
        Helper function for the function all_illnesses():
        this function creates in a recursive way a list of all illnesses
        in the tree and the number of times they appear.
        :param node: current node
        :type node: Node
        :param illnesses_dict: illnesses dictionary
        :type illnesses_dict: dict[str, int]
        """
        if node.negative_child is None and node.positive_child is None:
            if node.data is not None:
                if node.data not in illnesses_dict:
                    illnesses_dict[node.data] = 0
                illnesses_dict[node.data] += 1
            return

        self.__all_illnesses_helper(node.positive_child, illnesses_dict)
        self.__all_illnesses_helper(node.negative_child, illnesses_dict)

    def __transfer_dict_to_sorted_list(self, illnesses_dict):
        """
        This function sort the illnesses_dict by most common illnesses in the
        tree, and transform that dictionary to a list of illnesses.
        :param illnesses_dict: illnesses dictionary
        :type illnesses_dict: dict[str, int]
        :return: sorted by frequency list of illnesses
        :rtype: List[str]
        """
        sorted_dict = dict(
            sorted(illnesses_dict.items(), key=lambda item: item[1],
                   reverse=True))
        return [key for key in sorted_dict.keys()]

    def paths_to_illness(self, illness):
        """
        This function returns a list of all paths to the given illness.
        :param illness: illness
        :type illness: str or None
        :return: list of all paths to illness.
        :rtype: List[List[str]]
        """
        paths = []
        self.__path_to_illness_helper(self.root, illness, [], paths)
        return paths

    def __path_to_illness_helper(self, node, illness, curr_path, paths):
        """
        Helper function for the function paths_to_illness():
        this function finds in a recursive way all the paths to the given
        illness in the tree.
        :param node: current node
        :type node: Node
        :param illness: illness
        :type illness: str or None
        :param curr_path: current path to illness
        :type curr_path: List[bool]
        :param paths: list of all paths
        :type paths: List[List[bool]
        """
        if node.negative_child is None and node.positive_child is None:
            if node.data == illness:
                paths.append(curr_path[:])
            return

        curr_path.append(True)
        self.__path_to_illness_helper(node.positive_child, illness, curr_path,
                                      paths)
        curr_path.pop()
        curr_path.append(False)
        self.__path_to_illness_helper(node.negative_child, illness, curr_path,
                                      paths)
        curr_path.pop()

    def minimize(self, remove_empty=False):
        """
        This function replace our decision tree with a decision tree that has
        no redundant nodes. if remove_empty is False - remove question nodes
        that his decision doesn't matter for the diagnose. if remove_empty is
        True - same as False, with removing None Nodes.
        :param remove_empty: remove None Nodes.
        :type remove_empty: bool
        """
        self.__minimize_helper(remove_empty, self.root)

    def __minimize_helper(self, remove_empty, node):
        """
        Helper function for the function minimize():
        This function replace our decision tree with a decision tree that has
        no redundant nodes according to the remove_empty parameter.
        :param remove_empty: remove None Nodes.
        :type remove_empty: bool
        :param node: current node
        :type node: Node
        """
        if node.negative_child is None and node.positive_child is None:
            return

        self.__minimize_helper(remove_empty, node.positive_child)
        self.__minimize_helper(remove_empty, node.negative_child)

        # if subtree right is equal to subtree left:
        if self.__return_subtree(node.negative_child, []) == \
                self.__return_subtree(node.positive_child, []):
            node.data = node.negative_child.data
            node.negative_child = node.negative_child.negative_child
            node.positive_child = node.positive_child.positive_child
            return

        if remove_empty is True:
            if node.negative_child.data is None:
                node.data = node.positive_child.data
                node.negative_child = node.positive_child.negative_child
                node.positive_child = node.positive_child.positive_child
            elif node.positive_child.data is None:
                node.data = node.negative_child.data
                node.positive_child = node.negative_child.positive_child
                node.negative_child = node.negative_child.negative_child

    def __return_subtree(self, node, path):
        """
        This function find the path of a tree.
        :param node: current node
        :type node: Node
        :param path: current nodes tree path
        :type path: list[str]
        :return: list of the tree nodes data inorder
        :rtype: list[str]
        """
        if node:
            self.__return_subtree(node.positive_child, path)
            path.append(node.data)
            self.__return_subtree(node.negative_child, path)
        return path


def build_tree(records, symptoms):
    """
    This function build a tree that asks exactly about the symptoms in the list
    of symptoms in the order in which they appear, and return Diagnoser object
    for the tree being built.
    :param records: list of records
    :type records: list[Record]
    :param symptoms: list fo symptoms
    :type symptoms: List[str]
    :return: Diagnoser for the build tree
    :rtype: Diagnoser
    """
    if any(type(record) != Record for record in records):
        raise TypeError('not all records are type Record')
    if any(type(symptom) != str for symptom in symptoms):
        raise TypeError('not all symptoms are type string')
    root_node = _build_tree_helper(records, symptoms, [], 0)
    return Diagnoser(root_node)


def _build_tree_helper(records, symptoms, curr_path_symptoms, symptom_index):
    """
    Helper function for the function build_tree():
    The function build the tree in a recursive way, according to the given
    symptoms list and records.
    :param records: list of records
    :type records: list[Record]
    :param symptoms: list fo symptoms
    :type symptoms: List[str]
    :param curr_path_symptoms: list of path symptoms to leaf (illness)
    :type curr_path_symptoms: list[bool]
    :param symptom_index: current symptoms index
    :type symptom_index: int
    :return: Node
    :rtype: Node
    """
    if symptom_index == len(symptoms):
        # set dictionary of all matching illnesses to that leaf:
        matching_illnesses = set_matching_records_dict(records, symptoms,
                                                       curr_path_symptoms)
        if matching_illnesses == {}:  # if no illnesses found set leaf to None
            return Node(None, None, None)
        # take most frequent illness:
        illness = max(matching_illnesses, key=matching_illnesses.get)
        return Node(illness, None, None)

    curr_path_symptoms.append(True)
    left_child = _build_tree_helper(records, symptoms, curr_path_symptoms,
                                    symptom_index + 1)
    curr_path_symptoms.pop()
    curr_path_symptoms.append(False)
    right_child = _build_tree_helper(records, symptoms, curr_path_symptoms,
                                     symptom_index + 1)
    curr_path_symptoms.pop()
    return Node(symptoms[symptom_index], left_child, right_child)


def set_matching_records_dict(records, symptoms, symptoms_path):
    """
    This function set a dictionary of all records illnesses that match the path
    of the symptoms in the tree, and the count their appearance.
    :param records: list of records
    :type records: list[Record]
    :param symptoms: list fo symptoms
    :type symptoms: List[str]
    :param symptoms_path: list of path symptoms to leaf (illness)
    :type symptoms_path: list[bool]
    :return: dictionary of all matching illnesses, and their appearance count
    :rtype: dict[str, int]
    """
    records_dict = {}
    for record in records:
        if check_record_symptoms_match_to_path(record, symptoms,
                                               symptoms_path):
            if record.illness not in records_dict:
                records_dict[record.illness] = 0
            records_dict[record.illness] += 1
    return records_dict


def check_record_symptoms_match_to_path(record, symptoms, symptoms_path):
    """
    This function checks if the symptoms_path matches the record symptoms.
    :param record: record
    :type record: Record
    :param symptoms: list of symptoms
    :type symptoms: list[str]
    :param symptoms_path: symptoms path to leaf (illness)
    :type symptoms_path: list[bool]
    :return: True if matches, else False.
    :rtype: bool
    """
    for symptom_index in range(len(symptoms)):
        if (symptoms_path[symptom_index] is True and symptoms[
            symptom_index] not in record.symptoms) or \
                (symptoms_path[symptom_index] is False and
                 symptoms[symptom_index] in record.symptoms):
            return False
    return True


def optimal_tree(records, symptoms, depth):
    """
    The function returns a Diagnoser object for a tree with the highest success
    rate that askes a number symptoms equal to depth.
    :param records: list of records
    :type records: list[Record]
    :param symptoms: list fo symptoms
    :type symptoms: List[str]
    :param depth: size of sublist of symptoms to tree
    :type depth: int
    :return: Diagnoser for the build tree
    :rtype: Diagnoser
    """
    if depth < 0 or depth > len(symptoms):
        raise ValueError("value of depth is illegal")
    if len(set(symptoms)) != len(symptoms):
        raise ValueError("symptoms list contains duplicates")

    optimal_tree_comb = None
    optimal_tree_rate = 0
    for symptoms_comb in itertools.combinations(symptoms, depth):
        # built tree for the symptoms depth combination:
        comb_diagnoser = build_tree(records, symptoms_comb)
        # find success rate for that tree:
        comb_success_rate = comb_diagnoser.calculate_success_rate(records)
        # check if rate is higher than the current rate found:
        if comb_success_rate > optimal_tree_rate:
            optimal_tree_comb = comb_diagnoser
            optimal_tree_rate = comb_success_rate
    return optimal_tree_comb
