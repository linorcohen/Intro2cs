# def parentheses(n: int) -> List[str]:
#     """
#     This function receives an integer n and returns a list with all the strings
#     combinations with n valid (every opening brackets has closing brackets)
#     pairs of parenthesis.
#     :param n: number of brackets
#     :type n: int
#     :return: list of all combinations with n valid pairs of parenthesis.
#     :rtype: list[str]
#     """
#     results = []
#     _parentheses_helper(n, [], 0, 0, results)
#     return results
#
#
# def _parentheses_helper(n: int, seq: List[str], left_parens: int,
#                         right_parens: int, results: List[str]) -> None:
#     """
#     Helper function for the function parentheses():
#     The function finds in a recursive way all the possible combinations
#     with n valid pairs of parenthesis, and update the list of all combinations.
#     :param n: number of brackets
#     :type n: int
#     :param seq: current sequence of combination list
#     :type seq: List[str]
#     :param num_open: number of opening brackets
#     :type num_open: int
#     :param num_close: number of closing brackets
#     :type num_close: int
#     :param results: combinations results list
#     :type results: List[str]
#     """
#     if left_parens > right_parens:
#         return
#
#     if left_parens == 0 and right_parens == 0:
#         results.append(''.join(seq))
#         return
#
#     if left_parens > 0:
#         seq.append('(')
#         _parentheses_helper(n, seq, left_parens - 1, right_parens, results)
#         seq.pop()
#
#     if right_parens > 0:
#         seq.append(')')
#         _parentheses_helper(n, seq, left_parens, right_parens - 1, results)
#         seq.pop()
