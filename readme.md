# Project Folder Structure & Setup Instructions

## Folder Structure

```
project_root/
│── training/
│   ├── Code for training models using Sentence Transformer and Logistic Regression
│   ├── Includes regex-based classification code
│
│── models/
│   ├── Stores saved models, including:
│   ├── Sentence Transformer embeddings
│   ├── Logistic Regression model
│
│── resources/
│   ├── Contains resource files such as:
│   ├── Test CSV files
│   ├── Output files
│   ├── Images, etc.
│
│── app.py (Streamlit app code located in the root directory)
```

---

## Virtual Environment Setup

### Windows

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```sh
   venv\Scripts\activate
   ```

### Linux

1. Create a virtual environment:
   ```sh
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```sh
   source venv/bin/activate
   ```

---

## Install Dependencies

Run the following command to install all required dependencies:

```sh
pip install -r requirements.txt
```

---

## Run the Streamlit App

To start the application, run:

```sh
streamlit run app.py
```

