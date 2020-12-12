import calendar
import pickle
from datetime import timedelta
import pandas as pd
from scipy import sparse


def main(data):
    """"""
    df = pd.read_csv('./delay_app/airport_infos.csv')
    modelizer = pickle.load(open("./delay_app/prediction", 'rb'))
    categorical_list = get_categorical(data)
    my_array_categ = list_to_array(categorical_list)
    encoder = modelizer.get("encoding")
    encoded_array = encoder.transform(my_array_categ)
    list_num = transform_numerical_var(data, df)
    num_to_encod = list_to_array(list_num)
    num_transf = modelizer.get("normalizer")
    num_norm = num_transf.transform(num_to_encod)
    X_fin = construct_df(num_norm, encoded_array)
    X_final = X_fin.tocsr()
    model = modelizer.get("model")
    delay = model.predict(X_final)
    print(delay)
    return delay[0][0]


def get_categorical(dic):
    """Ce programme renvoie une liste ordonnée des informations nécessaires à la prédiction du retard.
    Pour ce faire on suit l'ordre des colonnes du dataframe initial. Pour y parvenir l'objectif est de récupérer
    ou calculer ces informations à partir des inputs de l'utilisateur entrée dans un dictionnaire. On récupérera ces valeurs
    à l'ide de leur clé puis de diverses transformations. Cela nécessitera de naviguer entre plusieurs types de variables,
    parfois travailler avec des float, des string et le module timedelta notamment pour les données horaires"""
    a = dic.get("date_year")
    b = dic.get("date_month")
    c = dic.get("date_day")
    infos = []
    infos.append(b)
    infos.append(c)
    day = calendar.weekday(a, b, c)
    day = day + 1
    infos.append(day)

    # uniquecarrier
    d = dic.get("company")
    e = dic.get("Airport_departure")
    f = dic.get("Airport_arrival")
    infos.append(d)
    infos.append(e)
    infos.append(f)
    return infos


def list_to_array(x):
    """"""
    my_array = pd.Series(x).values
    my_array = my_array.reshape(1, -1)
    return my_array


def transform_numerical_var(dic, df):
    """"""
    infos = []
    # distance
    distance = df.loc[(df['ORIGIN'] == dic.get("Airport_departure")) & (df['DEST'] == dic.get("Airport_arrival")),
                      'DISTANCE']
    distance = float(distance)
    infos.append(distance)
    # hour
    elapsed_time = df.loc[(df['ORIGIN'] == dic.get("Airport_departure")) & (df['DEST'] == dic.get("Airport_arrival")),
                          'CRS_ELAPSED_TIME']
    elapsed_time = float(elapsed_time)
    elapsed = float(elapsed_time)
    depart_hour = dic.get("hour")
    depart_hour = str(depart_hour)
    depart_minutes = dic.get("minutes")
    depart_minutes = str(depart_minutes)
    depart = depart_hour + depart_minutes
    depart = float(depart)
    infos.append(depart)
    dep_h = timedelta(minutes=depart)
    fly_time = timedelta(minutes=elapsed_time)
    arrival = dep_h + fly_time
    delta = arrival
    sec = delta.seconds
    hours = sec // 3600
    a = hours
    a = str(a)
    minutes = (sec // 60) - (hours * 60)
    b = minutes
    b = str(b)
    c = a + b
    c = float(c)
    infos.append(elapsed)
    infos.append(c)
    return infos


def construct_df(num, cat):
    X1 = sparse.csr_matrix(num)
    X_final = sparse.hstack((X1, cat))
    return X_final
