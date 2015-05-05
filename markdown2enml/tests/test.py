import unittest
import urllib
import StringIO

import markdown2enml
from lxml import etree

class ENMLValidationTest(unittest.TestCase):

    def setUp(self):
        self.dtd = etree.DTD(open('enml2.dtd'))

    def testValidXML(self):
        enml = markdown2enml.markdown("*boo!*")
        # lxml complains if we send a string, it wants an array of bytes
        root = etree.XML(enml.encode("UTF-8"))
        self.assertTrue(self.dtd.validate(root))
 
if __name__ == '__main__':
    unittest.main()
