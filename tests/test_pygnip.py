import os
import uuid
import json
from unittest import TestCase

import pygnip


class BasicTests(TestCase):
    _IS_SETUP = False

    def setUp(self):
        """
        Create a randomized uuid for the test tags and rules
        to be used in the tests
        """

        TestCase.setUp(self)

        test_uuid = str(uuid.uuid4())
        self.gnip_tag1 = "pygniptest-tag-%s" % test_uuid
        self.gnip_rule1 = "pygniptest-rule-%s" % test_uuid

        account_name = os.environ["GNIP_ACCOUNT_NAME"]
        username = os.environ["GNIP_USERNAME"]
        passwd = os.environ["GNIP_PASSWD"]

        self.gnip = pygnip.GnipPowerTrack(
            account_name=account_name,
            username=username,
            passwd=passwd)

        return True

    def testAddAndDeleteRule(self):

        r0 = self.gnip.getRules()
        print "Initial Count: %s" % len(r0)

        r1 = self.gnip.addRule(tag=self.gnip_tag1,
                               value=self.gnip_rule1)

        self.assertTrue(r1)
        r2 = self.gnip.getRules()
        self.assertEqual(len(r0)+1, len(r2))
        print "After Add: %s" % len(r2)

        r3 = self.gnip.removeRule(value=self.gnip_rule1)
        self.assertTrue(r3)
        r4 = self.gnip.getRules()
        self.assertEqual(len(r2)-1, len(r4))
        print "After Remove: %s" % len(r4)
