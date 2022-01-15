import pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, roc_auc_score


train = pd.read_csv("/content/train.csv")
test = pd.read_csv("/content/test.csv")


X = train.copy()
X_test = test.copy()

emp_type_encoder = LabelEncoder().fit(X['Employment Type'])

X['Employment Type'] = emp_type_encoder.transform(X['Employment Type'])
X['GraduateOrNot'] = X['GraduateOrNot'].map(lambda x: 1 if x == 'Yes' else 0)
X['FrequentFlyer'] = X['FrequentFlyer'].map(lambda x: 1 if x == 'Yes' else 0)
X['EverTravelledAbroad'] = X['EverTravelledAbroad'].map(lambda x: 1 if x == 'Yes' else 0)
y = X['TravelInsurance'].map(lambda x: 1 if x == 'Yes' else 0)
X = X.drop(['Customer Id', 'TravelInsurance'], axis=1)


X_test['Employment Type'] = emp_type_encoder.transform(X_test['Employment Type'])
X_test['GraduateOrNot'] = X_test['GraduateOrNot'].map(lambda x: 1 if x == 'Yes' else 0)
X_test['FrequentFlyer'] = X_test['FrequentFlyer'].map(lambda x: 1 if x == 'Yes' else 0)
X_test['EverTravelledAbroad'] = X_test['EverTravelledAbroad'].map(lambda x: 1 if x == 'Yes' else 0)

X, X_valid, y, y_valid = train_test_split(X, y, test_size=0.2, shuffle=True)

rf = RandomForestClassifier(n_jobs=-1, n_estimators=200, max_depth=3)
rf.fit(X, y)

valid_predicts = rf.predict(X_valid)
print("Accuracy: ", accuracy_score(y_valid, valid_predicts))


valid_probs = rf.predict_proba(X_valid)[:, 1]
print("ROC AUC: ", roc_auc_score(y_valid, valid_probs))


test_probs = rf.predict_proba(X_test.drop("Customer Id", axis=1))
X_test['prediction'] = test_probs[:, 1]
output = X_test[['Customer Id', 'prediction']]

output.to_csv("output.csv", index=False)

