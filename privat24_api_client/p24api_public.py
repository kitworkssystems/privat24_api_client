import datetime
import logging

from kws_date_ext import mining_date

from .p24api_base import Privat24Api

_logger = logging.getLogger(__name__)


class Privat24ApiPublic(Privat24Api):

    def exchange_rates(self, date=None):
        date = mining_date(date=date, silent=True) or datetime.date.today()
        return self.request_url(type_request='exchange_rates',
                                date=date.strftime('%d.%m.%Y'))
