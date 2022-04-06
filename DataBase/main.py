#
# @main.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from src.criteria import Criteria
from src.filters import Filters

# import pandas as pd
# excel = 'test/prueba.xlsx'
# df = pd.read_excel(excel)

if __name__ == '__main__':
    Criteria = Filters(6, 16, 'c', 'test/prueba.xlsx')
    print(Criteria.fil())
    # print(df[Criteria.fil()])
