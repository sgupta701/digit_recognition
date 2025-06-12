# train.py

import tensorflow as tf
from keras.activations import softmax

mnist = tf.keras.datasets.mnist

(X_train, y_train), (X_test,  y_test) = mnist.load_data()

X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)

#build model
model = tf.keras.models.Sequential()

#layer 1: Flatten layer
model.add(tf.keras.layers.Flatten())

#layer 2: Hidden layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

#layer 3: Hiddend layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

#layer 4: output latyer
model.add(tf.keras.layers.Dense(10, activation=softmax))

#compile model
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.fit(X_train, y_train, epochs=10)

test_loss, test_acc = model.evaluate(X_test,  y_test)

model.save("model-test.keras")

print("Accuracy", test_acc)
print("Loss", test_loss)


# Accuracy 0.9733999967575073
# Loss 0.11711640655994415