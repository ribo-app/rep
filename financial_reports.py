import pandas as pd 


def p_and_l_results(file_name):
    df = pd.read_csv(file_name)
    total_ingresos = df['total_fee'] + df['total_management_interest'] + df['total_management_fee']
    df['total_income'] = total_ingresos
    utilidad = df['total_income'] - df['total_cost']
    df['utilidad'] = utilidad 

    cols= df.columns.tolist()
    column_to_move = 'total_cost'
    new_position = 6


    cols.insert(new_position, cols.pop(cols.index(column_to_move)) )
    df= df[cols]

    return df.style.hide_index()

