import tensorflow as tf

model = tf.keras.models.load_model('modelbackups/2020-08-28 04:06:09.458051_sig_model.model')
rand = tf.random.normal([2, 8], 0, 2)
print(rand)
print(model(rand))