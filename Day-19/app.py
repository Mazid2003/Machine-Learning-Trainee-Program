from flask import Flask, request, render_template, redirect, url_for, session
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Create app
app = Flask(__name__)
app.secret_key = 'ccfe3aa0356e63f94f913df6f2b0b284'

# Load tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Load model
model = tf.keras.models.load_model('sentiment_lstm.h5')

# Parameters
MAX_LEN = 100  # Change if you used a different maxlen during training

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        
        # Tokenize and pad
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=MAX_LEN)
        
        # Predict
        pred_probs = model.predict(padded)[0]
        pred_class_idx = pred_probs.argmax()  # Assuming softmax
        label_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}  # Adjust if your model is binary

        pred_label = label_map.get(pred_class_idx, 'Unknown')

        # Store in session
        session['prediction'] = pred_label
        session['text'] = text

        return redirect(url_for('index'))
    
    prediction = session.pop('prediction', None)
    text = session.pop('text', '')
    return render_template('index.html', prediction=prediction, text=text)

if __name__ == '__main__':
    app.run(debug=True)
