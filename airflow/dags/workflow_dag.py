from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Project folder path
sys.path.append("c:/Users/syedz/Contents/Academia/Serve-Us/mlops_assignment3")

# Importing the data collection and preprocessing functions
from data_collection import collect_data  # Ensure this function exists in your project
from preprocessing import preprocess_data
from model_training import train_model

# Defining the DAG 
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    'data_collection_processing_dag',
    default_args=default_args,
    description='A DAG to collect and preprocess crypto data',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Data Collection
    data_collection_task = PythonOperator(
        task_id='collect_data_task',
        python_callable=collect_data,  # Function to collect data
    )

    # Task 2: Data Preprocessing
    data_preprocessing_task = PythonOperator(
        task_id='preprocess_data_task',
        python_callable=preprocess_data,  # Function to preprocess data
    )

    # Task 3: Model Training
    model_training_task = PythonOperator(
        task_id='train_model_task',
        python_callable=train_model,  # Function to train the model
    )

    # Setting task dependencies
    data_collection_task >> data_preprocessing_task >> model_training_task