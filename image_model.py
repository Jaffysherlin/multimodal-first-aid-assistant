import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np

# Load MobileNetV2 (for demo, can fine-tune with injury dataset)
model = MobileNetV2(weights="imagenet", include_top=True)

def predict_injury(img):
    img = img.resize((224,224))
    x = keras_image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    # For demo, return top predicted class name
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0][0][1]
    return decoded
