import pandas as pd
import datetime

def p_and_l_results(file_name):
    df = pd.read_csv(file_name)
    df.columns = ['month', 'year', 'total_fee', 'total_cost', 'total_management_interest', 'total_management_fee']
    df['day'] = 1
    
    date = pd.to_datetime(df[['year', 'month', 'day']])
    df = df.drop(['month', 'year', 'day'], axis=1)
    df['date'] = date
    df.set_index('date', inplace=True, drop=True)
    df = df.sort_index()
    df.sort_index(inplace=True)

    if file_name == "resultadosDR.csv":
        df = df.div(52)

    total_ingresos = df['total_fee'] + df['total_management_interest'] + df['total_management_fee']
    df['total_income'] = total_ingresos
    utilidad = df['total_income'] - df['total_cost']
    df['utilidad'] = utilidad

    

    cols= df.columns.tolist()
    column_to_move = 'total_cost'
    new_position = 4


    cols.insert(new_position, cols.pop(cols.index(column_to_move)))
    df= df[cols]


    return df




