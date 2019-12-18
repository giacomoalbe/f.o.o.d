from sales_prediction import predict, get_prediction_from_file

def getExpectationsData():
    colonne = get_prediction_from_file()

    graphData = {
        'dates': colonne['dates'],
        'sales': colonne['sales'],
        'prediction': colonne['prediction'],
    }

    return graphData
