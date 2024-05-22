import sklearn
import sklearn.ensemble._forest
from joblib import load
import pandas as pd
import datetime

# загружаем модель
model = load('model.joblib')

def start_model(start_date:datetime.date, end_date:datetime.date=None):
    if end_date is None:
        end_date = start_date
    date_list = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days+1)]
    X = pd.DataFrame({"Дата": date_list})
    X["Дата"] = pd.to_datetime(X["Дата"], format="%d.%m.%Y")
    return [X["Дата"], model.predict(pd.DataFrame({"Год": X["Дата"].dt.year, "Месяц": X["Дата"].dt.month, "День": X["Дата"].dt.day}))]

