import logging
from xml.etree import ElementTree

import requests

_logger = logging.getLogger(__name__)


class Privat24Api(object):
    BASE_URL = 'https://api.privatbank.ua/p24api/'
    HEADERS = {
        'User-Agent': 'python',
        'id': '',
        'Token': '',
        'Content-Type': 'application/json;charset=utf8',
        'Accept': 'application/json',
    }

    def request_url(self, type_request, **arg):
        url = '{}/{}'.format(self.BASE_URL, type_request)
        r = requests.get(url, params=arg, headers=self.HEADERS)
        if r.status_code in [200, 201]:
            try:
                tree = ElementTree.XML(r.text)
            except Exception as e:
                _logger.info('Parsing XML respond error %s', e)
                return r
            if tree.tag == 'error':
                raise Exception('Server respond error! %s', )
            return tree
        else:
            raise Exception(
                'Server respond error! Status code {}'.format(r.status_code))
