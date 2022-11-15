import unittest2
from examples import Example


class MyTestCase(unittest2.TestCase):
     def setUp(self):
         print("this will run before every method")
     def tearDown(self):
         print("this will run after every method")
     def test_add(self):
        self.assertEqual(Example.add(self,10,20),30)  # add assertion here
        self.assertEqual(Example.add(self, 0, 0),0)
     def test_sub(self):
        result=Example.sub(self,50,20)
        self.assertEqual(result,30)  # add assertion here

if __name__ == '__main__':
      unittest2.main()
