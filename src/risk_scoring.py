def risk_level(probability):

    if probability > 0.7:
        return "High Risk"

    elif probability > 0.4:
        return "Medium Risk"

    else:
        return "Low Risk"