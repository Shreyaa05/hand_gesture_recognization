import tensorflow as tf

# Path to your SavedModel folder
saved_model_path = "mp_hand_gesture"

# Load the model
model = tf.keras.models.load_model(saved_model_path, compile=False)

# Save as H5 file
model.save("mp_hand_gesture.h5")
print("✅ Model successfully converted to H5 format.")
