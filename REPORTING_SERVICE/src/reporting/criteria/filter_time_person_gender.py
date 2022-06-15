#
# @filters_time_person_gender.py Copyright (c)
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

import pandas as pd
from datetime import datetime


class FiltersStartFinishTimePersonGender:
    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time

    def filters_start_finish_time_person_gender(self, data_frame):
        df = data_frame
        morning = datetime.strptime(self.open_time, '%H:%M:%S').time()
        afternoon = datetime.strptime('12:00:00', '%H:%M:%S').time()
        night = datetime.strptime(self.close_time, '%H:%M:%S').time()
        filters_morning = (df["start_time"] >= morning) & \
                          (df["start_time"] < afternoon)
        filters_afternoon = (df["start_time"] >= afternoon) & (
                    df["start_time"] < night)
        df_m = df[filters_morning]
        df_a = df[filters_afternoon]

        graphs_morning = df_m.groupby(['person_gender']).size().reset_index(
            name='morning')
        graphs_afternoon = df_a.groupby(['person_gender']).size().reset_index(
            name='afternoon')
        data_result = pd.merge(graphs_morning, graphs_afternoon, on='person_gender')
        return data_result
