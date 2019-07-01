import unittest
from functions import *


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_get_document_owner(self):
        func_result = get_document_owner(documents)
        # здесь нужно ввести тот же номер документа, что и в проверяемой функции
        test_user_input = input('Повторите номер документа: ')
        for person in documents:
            if test_user_input in person:
                self.assertEqual(documents.index(func_result), documents.index(person))
        if test_user_input not in documents:
            self.assertEqual(func_result, None)

    def test_get_documents_info(self):
        func_result = get_documents_info(documents)
        self.assertEqual(len(documents), len(func_result))

    def test_get_shelf_number_by_document_number(self):
        func_result = get_shelf_number_by_document_number(directories)
        # здесь нужно ввести тот же номер документа, что и в проверяемой функции
        test_user_input = input('Повторите номер документа: ')
        for shelf in directories:
            if test_user_input in shelf:
                self.assertEqual(func_result, directories.index(shelf) + 1)

    def test_add_document_and_shelf(self):
        a = len(documents)
        b = len(directories)
        len_shelf_1 = len(directories['1'])
        len_shelf_2 = len(directories['2'])
        len_shelf_3 = len(directories['3'])
        add_document_and_shelf()
        self.assertEqual(len(documents), a + 1)
        if len(directories) == b:
            if len_shelf_1 < len(directories['1']):
                self.assertEqual(len_shelf_1 + 1, len(directories['1']))
            elif len_shelf_2 < len(directories['2']):
                self.assertEqual(len_shelf_2 + 1, len(directories['2']))
            elif len_shelf_3 < len(directories['3']):
                self.assertEqual(len_shelf_3 + 1, len(directories['3']))
        else:
            self.assertEqual(b + 1, len(directories))

    def test_main(self):
        func_result = main()
        # здесь нужно ввести тот же номер документа, что и в проверяемой функции
        test_user_input = input('Повторите команду: ')
        if test_user_input is 'p':
            self.assertEqual(func_result, get_document_owner(documents))
        if test_user_input is 'l':
            self.assertEqual(func_result, get_documents_info(documents))
        if test_user_input is 's':
            self.assertEqual(func_result, get_shelf_number_by_document_number(directories))
        if test_user_input is 'a':
            self.assertEqual(func_result, add_document_and_shelf())
        else:
            self.assertEqual(func_result, None)


if __name__ == '__main__':
    unittest.main()
