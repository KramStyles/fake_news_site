from tensorflow.keras.models import load_model
import pickle


from tensorflow.keras.preprocessing.sequence import pad_sequences

# Import tokenizer
with open('files/main_token.pkl', 'rb') as myfile:
    old_tokenizer = pickle.load(myfile)

# Bring in model
old_model = load_model('files/main_model.h5')


def check_news_auth(news_array):
    x = [news_array]
    x = old_tokenizer.texts_to_sequences(x)
    x = pad_sequences(x, 1000)
    x = (old_model.predict(x) >= 0.5).astype(int)
    if x[0][0] == 0:
        x = "News is fake"
    else:
        x = "News is real"
    return x

