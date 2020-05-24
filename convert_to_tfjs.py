from tensorflow import keras

#load keras/tensorflow model (e.g. 'model.h5')
model = keras.models.load_model('./keras-models/motorway_4ch.h5')

#create model in json format to specified folder
import tensorflowjs as tfjs
tfjs.converters.save_keras_model(model, './tfjs-models/')