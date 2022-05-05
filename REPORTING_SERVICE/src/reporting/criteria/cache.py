#
# @cache.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import pickle
from decouple import config

PICKLE_PATH = config('PICKLE_PATH')

class Cache:

    @staticmethod
    def write_cache(pd_data):
        outfile = open(PICKLE_PATH, 'wb')
        pickle.dump(pd_data, outfile)
        outfile.close()

    @staticmethod
    def load_cache():
        infile = open(PICKLE_PATH, 'rb')
        pd_cache = pickle.load(infile)
        infile.close()
        return pd_cache
