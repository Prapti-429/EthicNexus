import logging
import time

logging.basicConfig(
    filename="real_time_ai_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_decision(data, prediction):
    logging.info(f"Data: {data}, Prediction: {prediction}")
    print(f"Decision logged: {data}, Prediction: {prediction}")

if __name__ == "__main__":
    example_data = {"feature1": 0.5, "feature2": 1.2}
    example_prediction = "approved"
    log_decision(example_data, example_prediction)
