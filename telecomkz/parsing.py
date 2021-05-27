import os
from time import sleep
from typing import List

import attr
import requests

from telecomkz.authorization import TokenManager
from settings import URL_PATTERN, HEADERS
from utils import replace_fext, read_tsv, append_file, read_lines


@attr.s
class ClientInfo:
    customer_id = attr.ib(default='')
    local_abonent_id = attr.ib(default='')
    filial_id = attr.ib(default='')
    iin = attr.ib(default='')
    enriched_mobile_phone = attr.ib(default='')
    status = attr.ib(default='')


class TelecomkzApiParsing:
    def __init__(self, info: List, output_csv_fpath):
        # if os.path.exists(self.parsed_fpath):
        #     pass
        self.info = info
        self.output_csv_fpath = output_csv_fpath
        self.parsed_fpath = replace_fext(self.output_csv_fpath, '.prs')
        # if os.path.exists(self.parsed_fpath):
        #     parsed_info = read_lines(self.parsed_fpath)
        #
        #     self._parsed_info_count = len(parsed_info)
        #
        #     # source_bids = [bid for bid in read_lines(bids_fpath) if check_id(bid)]
        #     # self._source_bids_count = len(source_bids)
        #
        #     # excluding parsed bids
        #     if parsed_info:
        #         s = set(info)
        #         s.difference_update(set(parsed_bids))
        #         self._bids = deque(list(s))
        #     else:
        #         self._bids = deque(source_bids)

        self.http = TokenManager()

    def _prepare_info(self, src_info, parsed_info):
        pass

    def parse(self):
        for i in self.info:
            headers = HEADERS
            headers['Authorization'] = 'Bearer {}'.format(self.http.token)
            _i = ClientInfo(*i)
            url = URL_PATTERN.format(_i.iin, f'7{_i.enriched_mobile_phone}')
            r = requests.get(url, headers=headers, verify=False)
            print(r.json())
            if r.status_code == 200:
                _i.status = '1' if r.json()['data']['verification_state'] else '0'
                tpl = attr.astuple(_i)
                append_file(self.output_csv_fpath, ','.join(tpl))
            print(_i)
            sleep(1.5)
            print(url)


# rows = read_tsv('C:\\Users\\elessar\\bmg_1.csv')
rows = read_tsv(os.path.join(os.path.expanduser('~'), 'bmg_1.csv'))
# out_fpath = 'C:\\Users\\elessar\\out1.csv'
out_fpath = os.path.join(os.path.expanduser('~'), 'out1.csv')
p = TelecomkzApiParsing(rows, out_fpath)
p.parse()

