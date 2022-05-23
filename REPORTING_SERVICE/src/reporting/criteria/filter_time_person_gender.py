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
import time
import pandas as pd
from datetime import datetime


class FiltersStartFinishTimePersonGender:
    def __init__(self, open_time: time, close_time: time):
        self.open_time: time = open_time
        self.close_time: time = close_time

    def filters_start_finish_time_person_gender(self, data_frame) -> bool:
        df = data_frame
        morning: time = datetime.strptime(self.open_time, '%H:%M:%S').time()
        afternoon: time = datetime.strptime('12:00:00', '%H:%M:%S').time()
        night: time = datetime.strptime(self.close_time, '%H:%M:%S').time()
        filters_morning: bool = (df["start_time"] >= morning) & \
                                (df["start_time"] < afternoon)
        filters_afternoon: bool = (df["start_time"] >= afternoon) & (
                                   df["start_time"] < night)
        df_m: any = df[filters_morning]
        df_a: any = df[filters_afternoon]

        graphs_morning: any = df_m.groupby(['person_gender']).size().reset_index(
            name='morning')
        graphs_afternoon: any = df_a.groupby(['person_gender']).size().reset_index(
            name='afternoon')
        data_result: bool = pd.merge(graphs_morning, graphs_afternoon, on='person_gender')
        data_result.plot.bar(x='person_gender', title='Quantity vs Gender', stacked=True)

        return data_result
