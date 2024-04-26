from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import tensorflow as t

dataset=load_iris()
X=dataset.data
y=dataset.target
X_train,X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state=42)
pipeline=Pipeline([('scaler',preprocessing.StandardScaler()),('model',svm.SVC(kernel='linear'))])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

t_model = t.keras.models.Sequential([
    t.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    t.keras.layers.Dense(32, activation='relu'),
    t.keras.layers.Dense(3, activation='softmax')
])
t_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
t_model.fit(X_train, y_train, epochs=10)
t_model.evaluate(X_test, y_test)
tf_accuracy = t_model.evaluate(X_test, y_test, verbose=0)[1]
print("Accuracy (TensorFlow):", tf_accuracy)
  