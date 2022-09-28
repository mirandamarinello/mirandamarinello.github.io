import dominate
import pandas as pd
import numpy as np
from dominate.tags import *

df = pd.DataFrame()

docLi = ['about', 'art', 'contact', 'creations', 'embroidery', 'furniture-restoration', 'garments', 'icons', 'index', 'jewelry']
#print(len(docLi))

class Page:
    def __init__(self, pg):
        self.pgname = pg.lower()
        self.path = f'mirandamarinello.github.io/{pg.lower()}.html'
        self.doc = f'doc_{docLi.index(pg.lower())} = dominate.document(title=\'{pg.lower()}\')'
        self.pgcls = f'class = \'{pg.lower()}\''

for i in docLi:
    pg_i = Page(i)
    print(f'{docLi.index(i)}:\n  {pg_i.pgname}\n  {pg_i.path}\n  {pg_i.doc}\n  {pg_i.pgcls}\n')

#y = map(lambda i: print(i), docLi)

#y = map(lambda i: f'doc_{docLi.index(i)} = dominate.document(title=\'{i}\')', docLi)

    #print(f'doc_{docLi.index(i)} = dominate.document(title=\'{i}\')')
    #f'doc_{docLi.index(i)} = dominate.document(title=\'{i}\')'

#    print(f'with doc_{docLi.index(i)}.head:\n   link(rel=\'stylesheet\', href=\'miranda-style.css\')\n  script(type=\'text/javascript\', src=\'script.js\')')
#    print(f'\n with doc_{docLi.index(i)}:\n  with nav.add(ol()):\n    for {i} in [\'{docLi[]}')

# doc = dominate.document(title='this is the title')
