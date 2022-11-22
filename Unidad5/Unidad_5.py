# import the libraries

import logging
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
import pandas as pd


# logging

logger = logging.getLogger(__name__)
format = logging.Formatter('%(asctime)s-%(levelname)s-%(levelno)s-%(message)s')
logger.setLevel(logging.getLevelName('INFO'))

# handler

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)


# defining DAG arguments

default_args = {
 'owner': 'Alkemy_Prisma',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 'DAG_Unidad_5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)

# Tasks

@dag.task(task_id = "read_top10")
def read_top10():
    
    logger.info("...Procesando archivo...")
    

    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"
    
    try:
        df = pd.read_csv(url)

        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False).head(10)
        
        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format - Completar tu propia ubicación para guardar el archivo de salida
        logger.info(f"...Transformando el dataframe a archivo.xlsx...")


        
        logger.info("...El archivo se procesó correctamente...")
        # Logging message INFO Success --- Completar

    except:
        logger.error("Se produjo un error al procesar el archivo.")
        # Logging message ERROR Fail --- Completar
        
 

# task pipeline
read_top10()