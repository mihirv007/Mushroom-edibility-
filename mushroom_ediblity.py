import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import joblib
import time
import seaborn as sns
from seaborn import heatmap,pairplot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,f1_score,accuracy_score,classification_report


dataset=pd.read_csv("/Users/mihirverma/Mushroom_ediblity/mushroom_cleaned.csv")

# rows 54035 and 9 columns 
features=['cap-diameter', 'cap-shape', 'gill-attachment', 'gill-color', 'stem-height', 'stem-width', 'stem-color', 'season', 'class']


for value in features:
    print(f'max {value}:{max(dataset[value])}')
    print(f'min {value}:{min(dataset[value])}')

#axis 1 for column and axis 0 for row in drop

X=dataset.iloc[:,0:8]
y=dataset.iloc[:,8]

#spliting the dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#scaling the dataset
#normalize columns

normalize_columns=['cap-diameter','stem-width']
scaler=StandardScaler()

X_train[normalize_columns]=scaler.fit_transform(X_train[normalize_columns])
X_test[normalize_columns]=scaler.transform(X_test[normalize_columns])

#joblib.dump(scaler,'mushroom_scaler.pkl')

start_time=time.time()
print(f'start_time:{start_time}')
#Build the model
svm = SVC(kernel="rbf", gamma=0.5, C=1.0)

# Trained the model
svm.fit(X_train,y_train)

#joblib.dump(svm,'mushroom_model.pkl')

end_time=time.time()
print(f'end time:{end_time}')

print(f'execution time:{end_time - start_time:.2f}s')

test_predict=svm.predict(X_test)

confusion_Matrix=confusion_matrix(y_test,test_predict)
print(f'confusion:{confusion_Matrix}')

f1score=f1_score(y_test,test_predict)
print(f'f1_score:{f1score}')

accuracyscore=accuracy_score(y_test,test_predict)
print(f'accuracy:{accuracyscore}')

classificationreport=classification_report(y_test,test_predict)
print(f'classification report:{classificationreport}')






