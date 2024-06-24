import tensorflow as tf

# Load the model
model = tf.keras.models.load_model(r'C:\Skripsi\GenderClassification\res\family\gabor\fold-5\family-def-fold5.h5')

# Verify the model
model.summary()