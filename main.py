import os

from parsing import TelecomkzApiParsing
from utils import read_tsv


# rows = read_tsv('C:\\Users\\elessar\\bmg_1.csv')
rows = read_tsv(os.path.join(os.path.expanduser('~'), 'bmg_1.csv'))
# out_fpath = 'C:\\Users\\elessar\\out1.csv'
out_fpath = os.path.join(os.path.expanduser('~'), 'out1.csv')
p = TelecomkzApiParsing(rows, out_fpath)
p.parse()
