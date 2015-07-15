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

        account_name = os.environ["GNIP_ACCOUNT_NAME"]
        username = os.environ["GNIP_USERNAME"]
        passwd = os.environ["GNIP_PASSWD"]

        self.gnip = pygnip.GnipPowerTrack(
            account_name=account_name,
            username=username,
            passwd=passwd)

        return True

    def testAddAndDeleteRule(self):
        test_uuid = str(uuid.uuid4())
        gnip_tag1 = "pygniptest-tag-%s" % test_uuid
        gnip_rule1 = "pygniptest-rule-%s" % test_uuid

        r0 = self.gnip.getRules()
        print "Initial Count: %s" % len(r0)

        r1 = self.gnip.addRule(tag=gnip_tag1,
                               value=gnip_rule1)

        self.assertTrue(r1)
        r2 = self.gnip.getRules()
        self.assertEqual(len(r0)+1, len(r2))
        print "After Add: %s" % len(r2)

        r3 = self.gnip.removeRule(value=gnip_rule1)
        self.assertTrue(r3)

        r4 = self.gnip.getRules()
        self.assertEqual(len(r2)-1, len(r4))
        print "After Remove: %s" % len(r4)

    def testDeleteMultipleRules(self):
        test_uuid1 = str(uuid.uuid4())
        test_uuid2 = str(uuid.uuid4())

        gnip_tag1 = "pygniptest-tag-%s" % test_uuid1
        gnip_rule1 = "pygniptest-rule-%s" % test_uuid1

        gnip_tag2 = "pygniptest-tag-%s" % test_uuid2
        gnip_rule2 = "pygniptest-rule-%s" % test_uuid2

        # Get current rule count
        r0 = self.gnip.getRules()
        print "Initial Count: %s" % len(r0)

        # Insert test data
        self.assertTrue(self.gnip.addRule(tag=gnip_tag1, value=gnip_rule1))
        self.assertTrue(self.gnip.addRule(tag=gnip_tag2, value=gnip_rule2))

        # Make sure test data were added
        r1 = self.gnip.getRules()
        self.assertEqual(len(r0)+2, len(r1))
        print "After Add: %s" % len(r1)

        # Remove multiple rules
        self.assertTrue(self.gnip.removeRules([gnip_rule1, gnip_rule2]))

        # Confirm that test data were removed
        r2 = self.gnip.getRules()
        self.assertEqual(len(r1)-2, len(r2))
        print "After Remove: %s" % len(r2)

    def testDeleteNoneExistingRule(self):
        results = self.gnip.removeRule(value="N0nEx1STINGGnIPRuLEssS")
        self.assertTrue(results)


class UnauthorizedErrorTests(TestCase):
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
        passwd = "WR0oOOooNgP@aAsWO-0rddDDdd"

        self.gnip = pygnip.GnipPowerTrack(
            account_name=account_name,
            username=username,
            passwd=passwd)

        return True

    def testAddRule(self):
        with self.assertRaises(pygnip.exceptions.GnipUnauthorizedException):
            self.gnip.addRule(tag=self.gnip_tag1, value=self.gnip_rule1)

    def testRemoveRule(self):
        with self.assertRaises(pygnip.exceptions.GnipUnauthorizedException):
            self.gnip.removeRule(value=self.gnip_rule1)

    def testGetRules(self):
        with self.assertRaises(pygnip.exceptions.GnipUnauthorizedException):
            self.gnip.getRules()


class InvalidRulesErrorTests(TestCase):
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

    def testAddRuleBlank(self):
        with self.assertRaises(ValueError):
            self.gnip.addRule(tag=self.gnip_tag1, value="")

    def testRemoveRuleBlank(self):
        with self.assertRaises(ValueError):
            self.gnip.removeRule(value="")
