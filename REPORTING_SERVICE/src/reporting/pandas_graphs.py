#
# @pandas_graphs.py Copyright (c)
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

import json
import pandas as pd
from matplotlib import pyplot as plt
from src.reporting.criteria.cache import Cache


class Graphics():

    def create_graph(self):
        result = Cache.load_cache()
        df = pd.DataFrame(data=result)
        result_graphs = df.groupby(['person_gender']).size().reset_index(name='cantidad')
        plt.bar(result_graphs['person_gender'], result_graphs['cantidad'], color=['pink', 'blue'])
        # create the bar plot
        plt.xlabel("Genero")
        plt.ylabel("Cantidad")
        plt.title("Reporting server")
        plt.show()
        # the converts the graphic to json
        result_json = result_graphs.to_json(date_format="iso", orient="records")
        result_loaded = json.loads(result_json)
        return json.dumps(result_loaded)
