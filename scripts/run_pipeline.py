import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
import logging
from src import config
from src.make_model import train_model_lat_long,train_model_other,train_model_all
from src.make_model import load_data

# Set up logging
logging.basicConfig(filename='../logs/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    print("Starting Pipeline...")
    logging.info("Starting Pipeline...")

    print("Training the models...")
    logging.info("Training the models...")

    train_model_lat_long()
    train_model_other()
    train_model_all()
    
    print("Pipeline completed successfully.")
    logging.info("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
