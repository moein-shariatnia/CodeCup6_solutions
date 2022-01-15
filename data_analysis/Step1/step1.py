import pandas as pd

train = pd.read_csv("/content/train.csv")


# 1
rows, cols = train.shape

# 2
mean_income = int(train['AnnualIncome'].mean())

# 3
travelled_abroad = (train['EverTravelledAbroad'] == 'Yes').sum()

# 4
tmp = train['Employment Type'].value_counts()
common_emp_type = tmp.index[0]
emp_type_percentage = round(tmp.values[0] / tmp.values.sum() * 100, 2)

# 5
both_conditions = (train['ChronicDiseases'] == 1) & (train['TravelInsurance'] == 'Yes')
final_percentage = both_conditions.sum() / (train['ChronicDiseases'] == 1).sum()
final_percentage = round(final_percentage * 100, 2)

# Writing to the output file
with open("/content/output.txt", "w") as file:
    file.write(f"{rows} {cols}\n")
    file.write(f"{mean_income}\n")
    file.write(f"{travelled_abroad}\n")
    file.write(f"{common_emp_type} {emp_type_percentage}\n")
    file.write(f"{final_percentage}")