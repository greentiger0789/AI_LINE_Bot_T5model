from fastapi import FastAPI
from ml_api import schemas
from ml_api.ml import MockMLAPI
from transformers import T5Tokenizer

MODEL_DIR = "../content/model" 
tokenizer = T5Tokenizer.from_pretrained('sonoisa/t5-base-japanese') 

app = FastAPI()
ml = MockMLAPI()
model = ml.load(MODEL_DIR) # load weight or model instanse using joblib or pickle

@app.post('/prediction/online', response_model=schemas.Pred)
async def online_prediction(data: schemas.Data):
    text = data.data[0].text
    print(text)
    preds = ml.predict(text, model, tokenizer)
    print(preds)
    f = open('recievedmessage.tsv', 'a', encoding='utf-8') # 受け取ったテキストの保存
    f.write(text + "\t" + preds + "\n") # 本文，推論結果を書き込む
    f.close()
    return {"prediction": preds}