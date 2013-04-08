import unittest

from pyramid import testing

class ContactTypeTests(unittest.TestCase):

    def _getTargetClass(self):
        from .resources import Contact
        return Contact

    def _makeOne(self, firstname=u'fred', lastname=u'wesley', bio=u'some bio'):
        return self._getTargetClass()(firstname=firstname, lastname=lastname, bio=bio)

    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.firstname, u'fred')
        self.assertEqual(instance.lastname, u'wesley')
        self.assertEqual(instance.bio, u'some bio')

