# 推論コード
# 参考：https://note.com/npaka/n/n6df9ef13a0ed
import torch
import neologdn
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re

def predictid(text):

    # テキスト
    # text = "イベントはいつ始まりますか"
    text = neologdn.normalize(text)

    # テキストをテンソルに変換
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=16, truncation=True)

    # 推論
    model.eval()
    with torch.no_grad():
        summary_ids = model.generate(inputs) 
        summary = tokenizer.decode(summary_ids[0])
        # print(summary)
    return summary
