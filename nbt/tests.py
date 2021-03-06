from nbt import *
from nbt import _TAG_Numeric
import unittest
from StringIO import StringIO
from gzip import GzipFile

class ReadWriteTest(unittest.TestCase):     # test that we can read the test file correctly

    def testReadBig(self):
        mynbt = NBTFile("bigtest.nbt")
        self.assertTrue(mynbt.filename != None)
        self.assertEqual(len(mynbt.tags), 11)

    def testWriteBig(self):
        mynbt = NBTFile("bigtest.nbt")
        output = StringIO()
        mynbt.write_file(buffer=output)
        self.assertTrue(GzipFile("bigtest.nbt").read() == output.getvalue())

    def testWriteback(self):
        mynbt = NBTFile("bigtest.nbt")
        mynbt.write_file()

class TreeManipulationTest(unittest.TestCase):

    def setUp(self):
        self.nbtfile = NBTFile()

    def testRootNodeSetup(self):
        self.nbtfile.name = "Hello World"
        self.assertEqual(self.nbtfile.name, "Hello World")

    def testTagNumeric(self):
        for tag in TAGLIST:
            if isinstance(TAGLIST[tag], _TAG_Numeric):
                tagobj = TAGLIST[tag](name="Test", value=10)
                self.assertEqual(byte.name, "Test", "Name not set correctly for %s" % TAGLIST[tag].__class__.__name__)
                self.assertEqual(byte.value, 10, "Value not set correctly for %s" % TAGLIST[tag].__class__.__name__)
                self.nbtfile.tags.append(tagobj)

    #etcetera..... will finish later

    def tearDown(self):
        del self.nbtfile

class EmptyStringTest(unittest.TestCase):

    def setUp(self):
        self.golden_value = "\x0A\0\x04Test\x08\0\x0Cempty string\0\0\0"
        self.nbtfile = NBTFile(buffer=StringIO(self.golden_value))

    def testReadEmptyString(self):
        self.assertEqual(self.nbtfile.name, "Test")
        self.assertEqual(self.nbtfile["empty string"].value, "")

    def testWriteEmptyString(self):
        buffer = StringIO()
        self.nbtfile.write_file(buffer=buffer)
        self.assertEqual(buffer.getvalue(), self.golden_value)

if __name__ == '__main__':
    unittest.main()
