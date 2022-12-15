#importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

#loading the dataset
data = pd.read_csv('image_data.csv')

#splitting the dataset into training and testing sets
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
 
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
                plt.title('Classifier (Training set)')
plt.xlabel('Features')
plt.ylabel('Target')

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model using the training sets
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)
plt.title('Classifier (Training set)')
plt.xlabel('Features')
plt.ylabel('Target')

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model using the training sets
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision, what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall, what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))

# Model F1 Score, what is the harmonic mean of precision and recall?
print("F1 Score:",metrics.f1_score(y_test, y_pred))

# Model Confusion Matrix, what is the confusion matrix?
print("Confusion Matrix:",metrics.confusion_matrix(y_test, y_pred))

# Model Classification Report, what is the classification report?
print("Classification Report:",metrics.classification_report(y_test, y_pred))
# Model Accuracy Score, what is the accuracy score?
print("Accuracy Score:",metrics.accuracy_score(y_test, y_pred))

# Model Precision Score, what is the precision score?
print("Precision Score:",metrics.precision_score(y_test, y_pred))