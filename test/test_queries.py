import unittest
from mock import patch, Mock

from utils.db import dal, DataAccessLayer

from model.query_builder import QueryBuilder
import model.tree as t
from utils import util


class test_operations(unittest.TestCase):
    db = {
        'dialect': 'postgresql',
        'driver': 'psycopg2',
        'username': 'lucasdpn',
        'password': 'tet123456',
        'host': 'localhost',
        'port': '5432',
        'database': 'db_sql_alchemy',
    }
    dal.db_init(DataAccessLayer.str_connection(db))
    base_path = "test/config/"

    @staticmethod
    def get_operations(file_name):
        path = test_operations.base_path + file_name
        obj = util.load_json(path)
        tree = t.tree_builder(obj)
        return QueryBuilder(tree)

    def setUp(self):
        self.operations = None

    def test_op_great_equal(self):
        self.operations = test_operations.get_operations('great_equal.json')

    def test_op_bad_regions(self):
        self.operations = test_operations.get_operations('bad_regions.json')

    def test_op_combined_maps(self):
        self.operations = test_operations.get_operations('combined_maps.json')

    def test_op_footprint(self):
        self.operations = test_operations.get_operations('footprint.json')

    def test_op_footprint_inner(self):
        self.operations = test_operations.get_operations(
                'footprint_inner.json')

    def test_op_footrpint_left(self):
        self.operations = test_operations.get_operations(
                'footprint_left.json')

    def test_op_footprint_inner_left(self):
        self.operations = test_operations.get_operations(
                'footprint_inner_left.json')

    def tearDown(self):
        self.operations.drop_all_tables()


if __name__ == '__main__':
    unittest.main()
