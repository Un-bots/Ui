#[UI](https://github.com/Un-bots/Ui) ~ Ai Assistant 

## Install

```bash
pkg update && pkg upgrade -y
pkg install git python termux-api nano -y
```

## Clone Project

```bash
git clone https://github.com/Un-bots/Ui.git
cd Ui
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Add API Key

Open `config.py` and replace:

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

with your own API key.

## Run

```bash
python main.py
```

## Update

```bash
git pull
```


