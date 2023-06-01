from pathlib import Path
import os
import time
import logging
from .views import scrapper

logger = logging.getLogger(__name__)


def my_scheduled_job():
    logging.info("Cron job was called")

    BASE_DIR = Path(__file__).resolve().parent.parent
    # dir_path = '/media/shashwat/2E9AD3589AD31AE3/MiniProject/data'
    dir_path = os.path.join(BASE_DIR, 'data')

    current_time = time.time()

    # Get the list of all CSV files in the directory
    csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]

    # Loop through the CSV files and check their access time
    for file in csv_files:
        if file in ["oyo.csv", "yatra.csv"]:
            # Skip files named "oyo.csv" and "yatra.csv"
            continue
        file_path = os.path.join(dir_path, file)
        access_time = os.path.getatime(file_path)
        # Check if the file hasn't been accessed in the last three days
        if (current_time - access_time) // (24 * 3600) >= 3:
            # Delete the file
            os.remove(file_path)
        else:
            # Keep the file
            pass

    # Print a list of remaining files
    remaining_files = [f for f in os.listdir(dir_path) if f.endswith('.csv') and f not in ["oyo.csv", "yatra.csv"]]
    # print("Remaining files:")
    for data in remaining_files:
        print('Scrapping for city: ', data)
        data = data.replace('.csv', '').split('_')
        city = data[0]
        state = data[1]

        if '-' in state:
            state = state.replace('-', ' ')

        scrapper(city, state)
