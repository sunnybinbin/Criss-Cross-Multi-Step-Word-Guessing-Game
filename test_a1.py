"""
Tests for CSSE1001 / 7030 Assignment 1
"""

__author__ = "Steven Summers"


import inspect
import random
from pathlib import Path
from typing import Tuple

from testrunner import AttributeGuesser, OrderedTestCase, RedirectStdIO, TestMaster, skipIfFailed


SEED = 10017030


class A1:
    """ Just used for type hints """

    @staticmethod
    def select_word_at_random(word_select: str) -> str:
        pass

    @staticmethod
    def create_guess_line(guess_no: int, word_length: int) -> str:
        pass

    @staticmethod
    def display_guess_matrix(guess_no: int, word_length: int, scores: Tuple[int, ...]) -> None:
        pass

    @staticmethod
    def compute_value_for_guess(word: str, start_index: int, end_index: int, guess: str) -> int:
        pass

    @staticmethod
    def main() -> None:
        pass


class TestA1(OrderedTestCase):
    """ Base for all a1 test cases """

    a1: A1
    a1_support: ...


class TestDesign(TestA1):
    """ Checks A1 design compliance """

    def test_clean_import(self):
        """ test no prints on import """
        self.assertIsCleanImport(self.a1, msg="You should not be printing on import for a1.py")

    def test_functions_defined(self):
        """ test all functions are defined correctly """
        a1 = AttributeGuesser.get_wrapped_object(self.a1)
        for func_name, func in inspect.getmembers(A1, predicate=inspect.isfunction):
            num_params = len(inspect.signature(func).parameters)
            self.aggregate(self.assertFunctionDefined, a1, func_name, num_params, tag=func_name)

        self.aggregate_tests()

    def test_doc_strings(self):
        """ test all functions have documentation strings """
        a1 = AttributeGuesser.get_wrapped_object(self.a1)
        for attr_name, _ in inspect.getmembers(a1, predicate=inspect.isfunction):
            self.aggregate(self.assertDocString, a1, attr_name)

        self.aggregate_tests()


class TestFunctionality(TestA1):
    """ Base for all A1 functionality tests """

    TEST_DATA = (Path(__file__).parent / 'test_data').resolve()

    @staticmethod
    def set_seed(seed=SEED, skip_numbers=0):
        """ helper method for settings random seed """
        random.seed(seed)
        for _ in range(skip_numbers):
            random.random()  # skip next random number

    def load_test_data(self, filename: str):
        """ load test data from file """
        with open(self.TEST_DATA / filename, encoding='utf8') as file:
            return file.read()

    def write_test_data(self, filename: str, output: str):
        """ write test data to file """
        with open(self.TEST_DATA / filename, 'w', encoding='utf8') as file:
            file.write(output)


@skipIfFailed(TestDesign, TestDesign.test_functions_defined.__name__, tag=A1.select_word_at_random.__name__)
class TestSelectWordAtRandom(TestFunctionality):
    """ Tests select_word_at_random """

    def test_select_fixed(self):
        """ test select random word from fixed """
        self.set_seed()
        actual = self.a1.select_word_at_random('FIXED')
        self.assertEqual(actual, 'jousting')

    def test_select_arbitrary(self):
        """ test select random word from arbitrary """
        self.set_seed()
        actual = self.a1.select_word_at_random('ARBITRARY')
        self.assertEqual(actual, 'comrade')

    def test_select_fixed_2(self):
        """ test select random word from fixed 2 """
        self.set_seed(skip_numbers=5)
        actual = self.a1.select_word_at_random('FIXED')
        self.assertEqual(actual, 'cornmeal')

    def test_select_arbitrary_2(self):
        """ test select random word from arbitrary 2 """
        self.set_seed(skip_numbers=5)
        actual = self.a1.select_word_at_random('ARBITRARY')
        self.assertEqual(actual, 'unmasked')

    def test_none(self):
        """ test invalid word_select returns None """
        actual = self.a1.select_word_at_random('fixed')
        self.assertIsNone(actual)


@skipIfFailed(TestDesign, TestDesign.test_functions_defined.__name__, tag=A1.create_guess_line.__name__)
class TestCreateGuessLine(TestFunctionality):
    """ Tests create_guess_line """

    def test_1_6(self):
        """ test guess 1 length 6 """
        result = self.a1.create_guess_line(1, 6)
        self.assertEqual(result, 'Guess 1| * | * | - | - | - | - |')

    def test_1_9(self):
        """ test guess 1 length 9 """
        result = self.a1.create_guess_line(1, 9)
        self.assertEqual(result, 'Guess 1| * | * | - | - | - | - | - | - | - |')

    def test_6_6(self):
        """ test guess 6 length 6 """
        result = self.a1.create_guess_line(6, 6)
        self.assertEqual(result, 'Guess 6| * | * | * | * | * | * |')

    def test_9_9(self):
        """ test guess 9 length 9 """
        result = self.a1.create_guess_line(9, 9)
        self.assertEqual(result, 'Guess 9| * | * | * | * | * | * | * | * | * |')

    def test_4_7(self):
        """ test guess 4 length 7 """
        result = self.a1.create_guess_line(4, 7)
        self.assertEqual(result, 'Guess 4| - | - | * | * | * | * | - |')


@skipIfFailed(TestDesign, TestDesign.test_functions_defined.__name__, tag=A1.display_guess_matrix.__name__)
class TestDisplayGuessMatrix(TestFunctionality):
    """ Tests display_guess_matrix """

    def test_display_01(self):
        """ test display_guess_matrix guess 1 length 6 """
        with RedirectStdIO(stdinout=True) as stdio:
            result = self.a1.display_guess_matrix(1, 6, ())

        actual = stdio.stdinout
        expected = self.load_test_data('display_01.out')
        self.assertEqual(actual, expected)
        self.assertIsNone(result)

    def test_display_02(self):
        """ test display_guess_matrix guess 2 length 6  """
        with RedirectStdIO(stdinout=True) as stdio:
            result = self.a1.display_guess_matrix(2, 6, (0,))

        actual = stdio.stdinout
        expected = self.load_test_data('display_02.out')
        self.assertEqual(actual, expected)
        self.assertIsNone(result)

    def test_display_03(self):
        """ test display_guess_matrix guess 3 length 6 """
        with RedirectStdIO(stdinout=True) as stdio:
            result = self.a1.display_guess_matrix(3, 6, (26, 14))

        actual = stdio.stdinout
        expected = self.load_test_data('display_03.out')
        self.assertEqual(actual, expected)
        self.assertIsNone(result)

    def test_display_04(self):
        """ test display_guess_matrix guess 9 length 9 """
        with RedirectStdIO(stdinout=True) as stdio:
            result = self.a1.display_guess_matrix(9, 9, (26, 14, 0, 12, 14, 26, 0, 0))

        actual = stdio.stdinout
        expected = self.load_test_data('display_04.out')
        self.assertEqual(actual, expected)
        self.assertIsNone(result)


@skipIfFailed(TestDesign, TestDesign.test_functions_defined.__name__, tag=A1.compute_value_for_guess.__name__)
class TestComputeValueForGuess(TestFunctionality):
    """ Tests compute_value_for_guess """

    def test_no_score(self):
        """ test no score """
        actual = self.a1.compute_value_for_guess('aecdio', 1, 2, 'xy')
        self.assertEqual(actual, 0)

    def test_vowel_match_wrong_index(self):
        """ test vowel match wrong index """
        actual = self.a1.compute_value_for_guess('aecdio', 3, 4, 'ix')
        self.assertEqual(actual, 5)

    def test_vowel_match_index(self):
        """ test vowel match index """
        actual = self.a1.compute_value_for_guess('aecdio', 3, 4, 'xi')
        self.assertEqual(actual, 14)

    def test_consonant_match_wrong_index(self):
        """ test consonant match wrong index """
        actual = self.a1.compute_value_for_guess('aecdio', 3, 4, 'xd')
        self.assertEqual(actual, 5)

    def test_consonant_match_index(self):
        """ test consonant match index """
        actual = self.a1.compute_value_for_guess('aecdio', 3, 4, 'dx')
        self.assertEqual(actual, 12)

    def test_multiple_match(self):
        """ test multiple matches """
        actual = self.a1.compute_value_for_guess('aecdio', 1, 4, 'cedi')
        self.assertEqual(actual, 36)

    def test_guess_in_word_no_substring(self):
        """ test guess in word not substring """
        actual = self.a1.compute_value_for_guess('aecdio', 1, 2, 'ad')
        self.assertEqual(actual, 0)


@skipIfFailed(TestDesign, TestDesign.test_functions_defined.__name__, tag=A1.main.__name__)
class TestMain(TestFunctionality):
    """ Tests main """

    def _run_main(self, file_in: str, file_out: str, stop_early: bool):
        """ runs the main function and captures output """
        data_in = self.load_test_data(file_in)

        error = None
        result = None
        with RedirectStdIO(stdinout=True) as stdio:
            stdio.stdin = data_in
            try:
                result = self.a1.main()
            except EOFError as err:
                error = err

        # self.write_test_data(file_out, stdio.stdinout)
        expected = self.load_test_data(file_out)
        if error is not None and not stop_early:
            last_output = "\n".join(stdio.stdinout.rsplit("\n")[-22:])
            raise AssertionError(
                f'Your program is asking for more input when it should have ended\nEOFError: {error}\n\n{last_output}'
            ).with_traceback(error.__traceback__)

        return expected, result, stdio

    def assertMain(self, file_in: str, file_out: str, stop_early: bool = False):
        """ assert the main function ran correctly """
        expected, result, stdio = self._run_main(file_in, file_out, stop_early=stop_early)
        self.assertMultiLineEqual(stdio.stdinout, expected)
        if stdio.stdin != '':
            self.fail(msg="Not all input was read")
        self.assertIsNone(result, msg="main function should not return a non None value")

    def test_help(self):
        """ test main help action """
        self.assertMain('main_help.in', 'main_help.out', stop_early=True)

    def test_quit(self):
        """ test quit action """
        self.assertMain('main_quit.in', 'main_quit.out')

    @skipIfFailed(test_name=test_quit.__name__)
    def test_invalid(self):
        """ test invalid action """
        self.assertMain('main_invalid.in', 'main_invalid.out')

    @skipIfFailed(test_name=test_invalid.__name__)
    def test_invalid_multiple(self):
        """ test invalid action """
        self.assertMain('main_invalid_multi.in', 'main_invalid_multi.out')

    def test_main_fixed_win(self):
        """ test main FIXED win """
        self.set_seed()
        self.assertMain('main_fixed_win.in', 'main_fixed_win.out')  # jousting

    def test_main_arbitrary_win(self):
        """ test main ARBITRARY win """
        self.set_seed()
        self.assertMain('main_arbitrary_win.in', 'main_arbitrary_win.out')  # comrade

    def test_main_fixed_lose(self):
        """ test main FIXED lose """
        self.set_seed(skip_numbers=5)
        self.assertMain('main_fixed_lose.in', 'main_fixed_lose.out')  # cornmeal

    @skipIfFailed(test_name=test_main_fixed_win.__name__)
    def test_main_fixed_invalid_length(self):
        """ test main FIXED with invalid length """
        self.set_seed()
        self.assertMain('main_fixed_invalid_length.in', 'main_fixed_invalid_length.out')  # jousting


def main():
    """ run tests """
    test_cases = [
        TestDesign,
        TestSelectWordAtRandom,
        TestCreateGuessLine,
        TestDisplayGuessMatrix,
        TestComputeValueForGuess,
        TestMain
    ]

    master = TestMaster(max_diff=None,
                        suppress_stdout=True,
                        # ignore_import_fails=True,
                        timeout=1,
                        include_no_print=True,
                        scripts=[
                            ('a1', 'a1.py'),
                            ('a1_support', 'a1_support.py')
                        ])
    master.run(test_cases)


if __name__ == '__main__':
    main()
