def preprocessor_params(series):
    params=list()
    for element in series:
        try:
            params.append(int(element))
        except:
            params.append(element)
    return params
