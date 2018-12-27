import datetime
import logging
import unittest
from xml.etree import ElementTree

from privat24_api_client import Privat24ApiPublic

_logger = logging.getLogger(__name__)


class TestPrivat24ApiClient(unittest.TestCase):
    def setUp(self):
        pass

    def test_exchange_rates_api(self):
        api = Privat24ApiPublic()
        res = api.exchange_rates('01.12.2014')
        self.assertTrue(isinstance(res, ElementTree.Element), )
        self.assertEqual(res.tag, 'exchangerates', )
        res = api.exchange_rates('www')
        self.assertTrue(isinstance(res, ElementTree.Element), )
        self.assertEqual(res.attrib['date'],
                         datetime.date.today().strftime('%d.%m.%Y'), )


if __name__ == '__main__':
    unittest.main()
