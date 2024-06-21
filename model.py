import tensorflow as tf
import numpy as np

model=tf.keras.applications.MobileNetV2(weights="imagenet")

def process_image(image):
    
    image = image.resize((224, 224))
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
    

    predictions = model.predict(image_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)
    
    
    component_names = [pred[1] for pred in decoded_predictions[0]]
    return component_names