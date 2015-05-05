import unittest
import urllib
import StringIO

import markdown2enml
from lxml import etree

class ENMLValidationTest(unittest.TestCase):
    """Validate the xml output against the evernote DTD
    
    To avoid network access during testing, the evernote dtd and the
    entities is references have been stored locally. To make this work,
    I had to edit the enml2.dtd to reference the local entity files instead
    of referencing the ones on http://www.w3.org
    """

    def setUp(self):
        self.dtd = etree.DTD(open('enml2.dtd'))

    def testValidXML(self):
        enml = markdown2enml.markdown("*boo!*")
        # lxml complains if we send a string, it wants an array of bytes
        root = etree.XML(enml.encode("UTF-8"))
        self.assertTrue(self.dtd.validate(root))
 
if __name__ == '__main__':
    unittest.main()
