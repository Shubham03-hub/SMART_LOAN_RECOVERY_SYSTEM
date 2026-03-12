def recovery_plan(risk):

    if risk == "High Risk":
        return "Aggressive collection calls + Legal notice"

    elif risk == "Medium Risk":
        return "Frequent reminders + Loan restructuring"

    else:
        return "Normal follow-up"


# Test the function
risk_level = "High Risk"

action = recovery_plan(risk_level)

print("Risk Level:", risk_level)
print("Recommended Action:", action)