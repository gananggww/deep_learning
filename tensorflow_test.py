import tensorflow as tf
import matplotlib.pyplot as plt

hehe = tf.keras.datasets.mnist

(xtrain, ytrain), (xtest, ytest) = hehe.load_data()

print(len(xtest))
print(len(xtrain))


plt.imshow(xtest[120])
plt.show()