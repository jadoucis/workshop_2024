
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import nltk

nltk.download('stopwords')
nltk.download('punkt')

from tokenizer import tokenize

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

with open('lr_models.pkl', 'rb') as f:
    lr_models = pickle.load(f)

label_cols = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']


class TextData(BaseModel):
    text: str


app = FastAPI()


def predict_toxicity(comment, threshold=0.5):
    comment_tfidf = tfidf_vectorizer.transform([comment])
    is_toxic = 0
    for label in label_cols:
        probability = lr_models[label].predict_proba(comment_tfidf)[0][1]
        if probability >= threshold:
            is_toxic = 1
            break
    return is_toxic


@app.post('/predict')
async def predict(data: TextData):
    if not data.text:
        raise HTTPException(status_code=400, detail="Le champ 'text' est requis.")

    cleaned_text = " ".join(tokenize(data.text))

    is_toxic = predict_toxicity(cleaned_text)

    if is_toxic == 1:
        result = "Le commentaire est toxique."
    else:
        result = "Le commentaire n'est pas toxique."

    return {"text": data.text, "prediction": result}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
