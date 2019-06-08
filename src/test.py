import unittest
from solution import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):
    """
    Our basic test class
    """
    def test_0(self):
        result = InventoryAllocator({ "apple": 1}, [{ "name": "owd", "inventory": { "apple": 5} }])
        expected = [{'owd': {'apple': 1}}]
        self.assertEqual(result, expected)
    
    def test_1(self):
        result = InventoryAllocator({ "apple": 1}, [{ "name": "owd", "inventory": { "apple": 0} }])
        expected = []
        self.assertEqual(result, expected)    
        
    def test_2(self):

        result = InventoryAllocator({ "apple": 10}, [{ "name": "owd", "inventory": { "apple": 5} },
                                                           { "name": "dm", "inventory": { "apple": 5 }}])
        expected = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        self.assertEqual(result, expected)
    
    # No Inventory
    def test_3(self):
        result = InventoryAllocator({ "apple": 1}, [])
        expected = []
        self.assertEqual(result, expected)
    
    # Multiple Inventory
    def test_4(self):

        result = InventoryAllocator({ "apple": 10, "banana": 5}, [{ "name": "owd", "inventory": { "apple": 5, "banana": 2} },
                                                           { "name": "dm", "inventory": { "apple": 5, "banana": 3}}])
        expected = [{'owd': {'apple': 5, "banana": 2}}, {'dm': {'apple': 5, "banana": 3}}]
        self.assertEqual(result, expected)
    
    def test_5(self):

        result = InventoryAllocator({ "apple": 10, "banana": 10}, [{ "name": "owd", "inventory": { "apple": 5, "banana": 10} },
                                                           { "name": "dm", "inventory": { "apple": 5, "banana": 3}}])
        expected = [{'owd': {'apple': 5, "banana": 10}}, {'dm': {'apple': 5}}]
        self.assertEqual(result, expected)
        
    def test_6(self):

        result = InventoryAllocator({ "apple": 10, "banana": 10}, [{ "name": "owd", "inventory": { "apple": 5, "banana": 5} },
                                                           { "name": "dm", "inventory": { "apple": 5, "banana": 3}}])
        expected = []
        self.assertEqual(result, expected)
    
    def test_7(self):

        result = InventoryAllocator({ "apple": 10, "banana": 12}, [{ "name": "owd", "inventory": { "apple": 5, "banana": 10} },
                                                           { "name": "dm", "inventory": { "apple": 5, "banana": 2}}])
        expected = [{'owd': {'apple': 5, "banana": 10}}, {'dm': {'apple': 5, "banana": 2}}]
        self.assertEqual(result, expected)    


if __name__ == '__main__':
    print("Start test...")
    unittest.main()