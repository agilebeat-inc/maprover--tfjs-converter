from tensorflow import keras
model = keras.models.load_model('./keras-models/motorway_4ch.h5')

import tensorflowjs as tfjs
tfjs.converters.save_keras_model(model, tfjs_target_dir)