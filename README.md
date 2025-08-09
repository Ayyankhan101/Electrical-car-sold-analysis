# Electric Vehicle Population Analysis

This project analyzes the Electric Vehicle Population dataset to understand the trends and characteristics of electric vehicles.

## Dataset

The dataset used in this project is `Electric_Vehicle_Population_Data.csv`. It contains information about battery electric vehicles (BEVs) and plug-in hybrid electric vehicles (PHEVs) registered in Washington state. The original dataset was provided as `Electric_Vehicle_Population_Data.zip` and has been extracted.

## Analysis

The analysis is performed in the `e_car_analysis.ipynb` Jupyter notebook. The notebook covers the following steps:

1.  **Data Loading and Cleaning:** The dataset is loaded and cleaned to handle missing values.
2.  **Exploratory Data Analysis (EDA):** Visualizations are created to understand the distribution of electric vehicles, top manufacturers, popular models, and trends over the years.
3.  **Machine Learning Model:** A machine learning model is built to predict the electric vehicle type (BEV or PHEV) based on the vehicle's features.

## Dashboard

A professional one-page dashboard has been created using Dash to visualize key insights from the dataset. You can run the dashboard using the following command:

```bash
python dashboard.py
```

Once the dashboard is running, open your web browser and navigate to `http://127.0.0.1:8050/` to view it.

## Setup

To run the analysis and the dashboard, you need to have Python installed. You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

Then, you can open and run the `e_car_analysis.ipynb` notebook or run the `dashboard.py` application.