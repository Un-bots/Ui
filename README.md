# 🤖 UI ~Ai Assistant

A powerful AI Voice Assistant built with Python for Android (Termux).

---

# 📱 Requirements

- Android Phone
- Termux (F-Droid Version Recommended)
- Internet Connection
- G API Key

---

# 🚀 Installation

## Step 1 - Update Termux

```bash
pkg update && pkg upgrade -y
```

---

## Step 2 - Install Required Packages

```bash
pkg install git python termux-api nano -y
```

---

## Step 3 - Clone Repository

```bash
git clone https://github.com/Un-bots/Ui.git
```

---

## Step 4 - Open Project

```bash
cd Ui
```

---

## Step 5 - Upgrade Pip

```bash
python -m pip install --upgrade pip
```

---

## Step 6 - Install Python Packages

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Open config.py

```bash
nano config.py
```

Replace

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

with your Gemini API Key.

Save

CTRL + O

Press Enter

CTRL + X

---

# ▶ Run Jarvis

```bash
python main.py
```

---

# 🔄 Update Project

```bash
git pull origin main
```

or

```bash
git pull origin termux
```

---

# 📂 Project Structure

```
Ui/
│
├── main.py
├── ai.py
├── speech.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ❌ Common Errors

## Permission Denied

```bash
termux-setup-storage
```

---

## Update Packages

```bash
pkg update && pkg upgrade -y
```

---

## Install Missing Package

```bash
pip install package_name
```


---

## Reinstall Requirements

```bash
pip install -r requirements.txt --upgrade
```

---

# 🧹 Remove Project

```bash
cd ..
rm -rf Ui
```

---

# 📥 Clone Again

```bash
git clone https://github.com/Un-bots/Ui.git
cd Ui
```

---

# ❤️ Developed By

Un-bots
