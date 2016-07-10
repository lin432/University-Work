import squeal as s
import database
import unittest


class TestCartesianProduct(unittest.TestCase):

    def to_set_rows(self, diction):
        '''
        (dict str:list of str) -> (set{str},[keys])
        '''

        length = 0
        key_length = 0
        for key in diction:
            key_length += 1
            if(len(diction[key]) > length):
                length = len(diction[key])

        ret_set = set()
        keys = []
        for index in range(0, length):
            string = ''
            for key in diction:
                keys += [key]
                string += diction[key][index] + ','

            ret_set.add(string[:len(string)-1])

        return (ret_set, keys[0:key_length])

    def get_expected(self, keys, e_dict):

        length = 0
        for key in e_dict:
            if(len(e_dict[key]) > length):
                length = len(e_dict[key])

        ret_set = set()
        for index in range(0, length):
            string = ''
            for key in keys:
                string += e_dict[key][index] + ','

            ret_set.add(string[:len(string)-1])

        return ret_set

    def test_all_keys(self):
        dict1 = {'table1.a': ['a', 'b']}
        dict2 = {'table2.1': ['1', '2']}
        table1 = database.Table()
        table2 = database.Table()
        table1.set_dict(dict1)
        table2.set_dict(dict2)

        result = s.cartesian_product(table1, table2)
        result_dict = result.get_dict()
        result_set_keys = result_dict.keys()

        expected = {'table1.a', 'table2.1'}

        self.assertEqual(result_set_keys, expected,
                         "Missing/non-identical keys")

    def test_proper_output(self):
        dict1 = {'table1.a': ['a', 'b', 'c']}
        dict2 = {'table2.1': ['1', '2', '3']}
        table1 = database.Table()
        table2 = database.Table()
        table1.set_dict(dict1)
        table2.set_dict(dict2)

        result = s.cartesian_product(table1, table2)
        r_dict = result.get_dict()

        keys = []
        r_set = set()
        (r_set, keys) = self.to_set_rows(r_dict)

        e_dict = {'table1.a': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
                  'table2.1': ['1', '2', '3', '1', '2', '3', '1', '2', '3']}

        e_set = self.get_expected(keys, e_dict)

        self.assertEqual(r_set, e_set, "improper output")

    def test_multiple_iterations(self):
        dict1 = {'table1.a': ['a', 'b']}
        dict2 = {'table2.1': ['1', '2']}
        dict3 = {'table3.x': ['x', 'y']}
        dict4 = {'table4.9': ['9', '0']}
        table1 = database.Table()
        table2 = database.Table()
        table3 = database.Table()
        table4 = database.Table()
        table1.set_dict(dict1)
        table2.set_dict(dict2)
        table3.set_dict(dict3)
        table4.set_dict(dict4)

        cart_table = s.cartesian_product(table1, table2)
        cart_table = s.cartesian_product(cart_table, table3)
        cart_table = s.cartesian_product(cart_table, table4)

        expected = (['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
                     'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                    ['1', '1', '1', '1', '2', '2', '2', '2',
                     '1', '1', '1', '1', '2', '2', '2', '2'],
                    ['x', 'x', 'y', 'y', 'x', 'x', 'y', 'y',
                     'x', 'x', 'y', 'y', 'x', 'x', 'y', 'y'],
                    ['9', '0', '9', '0', '9', '0', '9', '0',
                     '9', '0', '9', '0', '9', '0', '9', '0'])
        cart_dict = cart_table.get_dict()

        keys = []
        r_set = set()
        (r_set, keys) = self.to_set_rows(cart_dict)

        e_dict = {'table1.a': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
                               'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                  'table2.1': ['1', '1', '1', '1', '2', '2', '2', '2',
                               '1', '1', '1', '1', '2', '2', '2', '2'],
                  'table3.x': ['x', 'x', 'y', 'y', 'x', 'x', 'y', 'y',
                               'x', 'x', 'y', 'y', 'x', 'x', 'y', 'y'],
                  'table4.9': ['9', '0', '9', '0', '9', '0', '9', '0',
                               '9', '0', '9', '0', '9', '0', '9', '0']}

        e_set = self.get_expected(keys, e_dict)

        self.assertEqual(r_set, e_set, "output mismatch with key")

    def test_single_input(self):
        dict1 = {'table1.a': ['a']}
        dict2 = {'table2.1': ['1']}
        table1 = database.Table()
        table2 = database.Table()
        table1.set_dict(dict1)
        table2.set_dict(dict2)

        result = s.cartesian_product(table1, table2)
        result_dict = result.get_dict()

        keys = []
        r_set = set()
        (r_set, keys) = self.to_set_rows(result_dict)

        e_dict = {'table1.a': ['a'], 'table2.1': ['1']}

        e_set = self.get_expected(keys, e_dict)

        self.assertEqual(r_set, e_set, "output mismatch with key")

    def test_multiple_keys(self):
        dict1 = {'table1.a': ['a', 'b'], 'table3.x': ['x', 'y']}
        dict2 = {'table2.1': ['1', '2'], 'table4.9': ['9', '0']}
        table1 = database.Table()
        table2 = database.Table()
        table1.set_dict(dict1)
        table2.set_dict(dict2)

        result = s.cartesian_product(table1, table2)
        result_dict = result.get_dict()

        keys = []
        r_set = set()
        (r_set, keys) = self.to_set_rows(result_dict)

        e_dict = {'table1.a': ['a', 'a', 'b', 'b'],
                  'table3.x': ['x', 'x', 'y', 'y'],
                  'table2.1': ['1', '2', '1', '2'],
                  'table4.9': ['9', '0', '9', '0']}

        e_set = self.get_expected(keys, e_dict)

        self.assertEqual(r_set, e_set,
                         "Some or all columns were not multiplied properly")


if __name__ == '__main__':
    unittest.main()
