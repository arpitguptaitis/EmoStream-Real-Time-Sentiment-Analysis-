import requests
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def monitor_subscriptions(subscription_url="http://localhost:5002"):
    """Monitor and print subscription updates from the server"""
    logger.info("Starting subscription monitor...")
    
    while True:
        try:
            response = requests.get(f"{subscription_url}/subscriptions")
            if response.status_code == 200:
                subscriptions = response.json()
                logger.info(f"Current subscriptions: {subscriptions}")
            else:
                logger.error(f"Failed to get subscriptions. Status code: {response.status_code}")
        
        except Exception as e:
            logger.error(f"Error getting subscriptions: {str(e)}")
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    try:
        monitor_subscriptions()
    except KeyboardInterrupt:
        logger.info("Subscription monitor terminated")
