# AI_LINE_Bot_T5model

GoogleのT5（Text-to-Text Transfer Transformer）を用いてLINEで受け取ったメッセージの文章分類を行う．

FastAPIを用いてWeb API化し，HTTPプロトコルを用いて送受信を行う．

## Features

### 全体像

![OCdemoModel説明S](https://user-images.githubusercontent.com/51241162/129188640-2239f26b-5844-4129-9825-4616841a29b3.png)

[T5の日本語事前学習済みモデル](https://qiita.com/sonoisa/items/a9af64ff641f0bbfed44)をお借りしました．

WebAPI化のため，FastAPIを用いています．

ngrokを用いてhttpsでAPIをWANに公開することで，herokuなどからHTTPプロトコルを用いてアクセス可能です．

## Requirement

- Python3.9.2

- transformers==4.4.2
- torch==1.7.1+cu110
- torchtext==0.8.0
- torchvision==0.8.2
- neologdn==0.5.1
- pydantic==1.8.2
- fastapi==0.68.0
- pytorch_lightning==1.2.1
- sentencepiece==0.1.96

## Installation

```bash
pip install -r requirements.txt
```

```bash
brew install ngrok
```

## Usage

1. `textdataset.tsv`作成後，`T5_text_classification.ipynb'`を実行．
2. `オンライン予測WebAPI`ディレクトリに移動，`uvicorn main:app –-reload`でAPIをLANに公開．
3. `ngrok http 8000`でWANに公開（Windowsの場合，`./ngrok http 8000`）．


## Note

`textdataset.tsv`は以下のようにする．
```
メッセージ1<タブ>1<タブ>メッセージ1の正解ラベル</n>
メッセージ2<タブ>1<タブ>メッセージ2の正解ラベル</n>
・
・
・
```


APIをWANに公開したあと，コマンドラインから直接動作確認する場合は以下のようにする．

```bash
curl -X POST "https://<ここにngrokで発行したURLの一部を>.ngrok.io/prediction/online" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[{\"text\":\"イベントはいつ始まりますか（←例文）\"}]}" -w  "\n"
```

フロントエンド側（LINE DevelopersのMessaging API），Herokuとの接続方法の詳細は[共同制作者のリポジトリ](https://github.com/IoriKobayashi1998/kitakyu_bot_frontend)に公開している．

## Author

* [@greentiger0789](https://github.com/greentiger0789)

共同製作者
* [@IoriKobayashi1998](https://github.com/IoriKobayashi1998)
