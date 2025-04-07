import re
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s -%(message)s')


class LaunchAuthorizationSystem:
    """Handles nuclear launch authorization validation."""
    
    AUTH_PATTERN = r"^AUTH-[A-Z0-9]{6}-\d{4}-SECURE$"

    @staticmethod
    def validate_code(code):

        """Validates the launch authorization code."""
    
        logging.info("validating the logging info")

        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code):
            logging.info("authorization validation is successfull")
            return True

        else:
            logging.warning("authorization falied")
            return False

