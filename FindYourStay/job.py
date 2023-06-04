from pathlib import Path
import os
import time
import logging
from .views import scrapper
# from ..FindYourStay.views import scrapper


logger = logging.getLogger(__name__)


def the_job():
    logging.info("Cron job was called")

    # BASE_DIR = Path(__file__).resolve().parent.parent
    # print(BASE_DIR)
    
    dir_path = os.path.join(Path(__file__).resolve().parent.parent, 'data')
    # dir_path = '/media/shashwat/2E9AD3589AD31AE3/MiniProject/data'
    print(dir_path) 
    print()

    current_time = time.time()
    print(current_time)

    # Get the list of all CSV files in the directory
    csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]
    print(csv_files)
    print()

    # Loop through the CSV files and check their access time
    for file in csv_files:
        if file in ["oyo.csv", "yatra.csv"]:
            # Skip files named "oyo.csv" and "yatra.csv"
            continue
        file_path = os.path.join(dir_path, file)
        access_time = os.path.getatime(file_path)

        print(file, access_time, (current_time - access_time) // (24 * 3600), (current_time - access_time) // (24 * 3600) >= 3)
        # Check if the file hasn't been accessed in the last three days
        if (current_time - access_time) // (24 * 3600) >= 3:
            # Delete the file
            os.remove(file_path)
        else:
            # Keep the file
            pass
    
    print()
    
    # List of remaining files
    csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv') and f not in ["oyo.csv", "yatra.csv"]]
    print(csv_files)
    print()

    for file in csv_files:
        print('Scrapping for city: ', file)
        file = file.replace('.csv', '').split('_')
        city = file[0]
        state = file[1]

        if '-' in state:
            state = state.replace('-', ' ')

        scrapper(city, state)

    print("Job successfull!!")
