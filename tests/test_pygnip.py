import os
import uuid
from unittest import TestCase

import pygnip


class BasicTests(TestCase):

    def setUp(self):
        """
        Generate a queuename for this test (with random uuid)
        """

        test_uuid = uuid.uuid4()
        self.gnip_tag1 = "pygniptest%s" % str(test_uuid)
        self.gnip_rule1 = "pygniptest%s" % str(test_uuid)

        account_name = os.environ["GNIP_ACCOUNT_NAME"]
        username = os.environ["GNIP_USERNAME"]
        passwd = os.environ["GNIP_PASSWD"]

        self.gnip = pygnip.GnipPowerTrack(
            account_name=account_name,
            username=username,
            passwd=passwd)

    def test_add_rule(self):
        """
        length() must return 0 if queue is empty/not yet in redis
        """

        # self.gnip.addRule(tag=self.gnip_tag1,
        #                   value=self.gnip_rule1)
