# 🚀 SupplyMind AI

## AI-Powered Supply Chain Intelligence Platform

SupplyMind AI is an intelligent supply chain analytics platform designed to transform raw supply chain data into meaningful business insights using **data analytics, SQL, machine learning, visualization, and AI technologies**.

The platform analyzes customer behavior, sales performance, delivery risks, and supply chain operations to help organizations make data-driven decisions.

---

# 📌 Project Overview

Supply chains generate large volumes of data across orders, customers, products, shipments, and financial transactions. Extracting useful insights from this data manually is challenging.

SupplyMind AI addresses this challenge by building an end-to-end analytics solution that includes:

- Data preprocessing and ETL pipelines
- Exploratory data analysis
- SQL-based business analytics
- Machine learning-based delivery risk prediction
- Interactive Power BI dashboard
- AI-powered supply chain assistant (in development)

---

# 🎯 Problem Statement

Organizations face difficulties in:

- Identifying factors affecting delivery delays
- Understanding customer and product performance
- Tracking sales and operational KPIs
- Extracting actionable insights from large supply chain datasets

SupplyMind AI helps solve these challenges by combining analytics and machine learning techniques.

---

# ✨ Features

## 📊 Supply Chain Analytics

Implemented analytics for:

- Sales performance analysis
- Revenue trends
- Customer analysis
- Product performance analysis
- Delivery performance analysis
- Regional supply chain insights
- Operational KPI tracking


## 🤖 Machine Learning Delivery Risk Prediction

A machine learning model is developed to predict delivery risks using historical supply chain data.

### Model Used:
- XGBoost Classifier

### Prediction Objective:
- Predict late delivery risk

### ML Workflow:

```
Data Collection
      |
      ↓
Data Cleaning
      |
      ↓
Feature Engineering
      |
      ↓
Model Training
      |
      ↓
Delivery Risk Prediction
```

---

## 📈 Power BI Dashboard

An interactive Power BI dashboard was created to visualize supply chain performance.

Dashboard includes:

- Revenue analysis
- Sales trends
- Delivery risk analysis
- Customer insights
- Product performance
- Regional analysis

---

# 🏗️ System Architecture

```
                Supply Chain Dataset
                        |
                        ↓
              Data Processing Pipeline
                        |
                        ↓
              PostgreSQL Database
                        |
          ---------------------------
          |                         |
          ↓                         ↓
    SQL Analytics          ML Prediction Model
          |                         |
          ↓                         ↓
    Business Insights      Delivery Risk Prediction
          |
          ↓
     Power BI Dashboard
```

---

# 🛠️ Tech Stack

## Programming Languages

- Python
- SQL


## Data Processing

- Pandas
- NumPy


## Database

- PostgreSQL


## Machine Learning

- Scikit-learn
- XGBoost


## Visualization

- Power BI
- Matplotlib


## Backend & AI (Development)

- FastAPI
- Google Gemini API


## Tools

- Git
- GitHub
- VS Code
- Jupyter Notebook

---

# 📂 Project Structure

```
SupplyMind AI
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── model_loader.py
│   ├── llm.py
│   ├── chatbot.py
│   ├── database
│   └── etl
│
├── data
│   ├── raw
│   └── processed
│
├── models
│   └── ML model files
│
├── notebooks
│   ├── 01_Data_Exploration.ipynb
│   └── 02_ML_Delivery_Prediction.ipynb
│
├── powerbi
│   └── SupplyMind AI.pbix
│
├── sql
│   ├── KPI Analysis
│   ├── Sales Analysis
│   ├── Customer Analysis
│   ├── Supply Chain Analysis
│   └── ML Dataset Preparation
│
├── requirements.txt
└── README.md
```

---

# 🔄 Data Pipeline

```
Raw Supply Chain Dataset
          |
          ↓
Data Cleaning & Transformation
          |
          ↓
Processed Data
          |
          ↓
PostgreSQL Database
          |
          ↓
SQL Analytics + ML Model
          |
          ↓
Power BI Dashboard
```

---

# 🗄️ SQL Analytics

SQL analysis performed includes:

- Revenue analysis
- Monthly sales trends
- Customer analysis
- Product performance analysis
- Supply chain KPIs
- Delivery analysis
- Advanced analytical queries

---

# 📊 Machine Learning Model

The ML model predicts delivery risks based on historical order information.

Steps performed:

- Data preprocessing
- Feature selection
- Model training
- Model evaluation
- Prediction generation

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/rithikaranir/SupplyMind-AI.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📂 Dataset

Dataset used:

**DataCo Supply Chain Dataset**

The dataset contains information about:

- Orders
- Customers
- Products
- Shipments
- Sales
- Delivery status

---

# 🚀 Future Improvements

The following features are planned for future development:

- AI-powered supply chain chatbot
- Hybrid RAG implementation for document and database-based question answering
- Natural language querying of supply chain data
- Automated business recommendations
- Real-time delivery risk monitoring
- Demand forecasting
- Cloud deployment
- Real-time alerts and notifications

---

# 👩‍💻 Author

**Rithika Rani R**

B.Tech Computer Science and Information Technology

---

⭐ If you find this project useful, consider giving it a star!
