# fake-news-flask-detection-inference-ibr

Detects Fake News using Random Forest, CatBoost and Logistic Regression

This work trains Random Forest and CatBoost Ensemble algorithms on two datasets 

## Dataset Sources
- [Kaggle - ISOT Fake News Dataset](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets/data)
- [Kaggle - COVID-19 Dataset]()


## Install dependencies
- Make sure to have Python and Pip installed.
- Provided you already installed Python and Pip on your system
- Cloning this repository, open terminal (for MacOS and Linux users) or Command Prompt/Powershell (for Windows users) 
- Navigate to the main directory
- Run the command below:

```bash
pip install -r requirements.txt
```

## Runing the Inference App Backend Server 
To start the inference app server, run the following command:

```bash
python ./app.py
```

## Making requests to the Web App for prediction

Host: `http://127.0.0.1:5000`
---

- Access the Home Page Interface for prediction on the web browser
Endpoint: `GET /`

- Post a news for detection
Endpoint: `POST /classify-news`
Payload:
```json
{
    "news": "news article to classify here ...",
    "model": "model type to use"
}

_NOTE:_ Model can be any of `rf` for Random Forest, `cb` for CatBoost, `logreg` for Logistic Regression or `best` for best model i.e. Random Forest.




