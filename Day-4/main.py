# main.py
import json
import logging
from authorization import LaunchAuthorizationSystem

# Set up logging for console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Warhead:
    """Represents a nuclear warhead with specific payload information."""
    
    def __init__(self, warhead_id, type, yield_kt):
        self.warhead_id = warhead_id
        self.type = type
        self.yield_kt = yield_kt  

    def get_info(self):
        return f"Warhead {self.warhead_id}: Type {self.type}, Yield {self.yield_kt}kt"


class Submarine:
    """Controls the nuclear missile launch sequence."""
    
    def __init__(self, name, warhead_data):
        self.name = name
        self.warheads = [Warhead(**w) for w in warhead_data]
        self.failed_attempts = 0

    def authorize_launch(self, auth_code):
        logging.info(f"Launch authorization attempt initiated by {self.name}.")
        
        if LaunchAuthorizationSystem.validate_code(auth_code):
            self.failed_attempts = 0  # reset on success
            logging.info(f"Launch authorized for {self.name}. Preparing to launch SLBM...")
            if self.warheads:
                warhead = self.warheads[0] 
                logging.info(f"Missile launched carrying {warhead.get_info()}!")
            else:
                logging.error("No warheads available for launch.")
        else:
            self.failed_attempts += 1
            logging.error("Launch Authorization Failed! Access Denied.")
            if self.failed_attempts >= 3:
                self.self_destruct()

    def self_destruct(self):
        logging.critical(f"Unauthorized attempts exceeded limit on {self.name}. Initiating self-destruct sequence!")
        # Simulate self-destruct
        print("Self-destruct initiated! System lockdown in progress...")


# JSON Data (Simulating a warhead payload inventory)
warhead_json = '''
[
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''

# Load warhead data
warhead_data = json.loads(warhead_json)

# Initialize submarine
submarine = Submarine("USS Trident", warhead_data)

# 🚀 Try launching with an incorrect code (3 times to trigger self-destruct)
submarine.authorize_launch("INVALID-123")
submarine.authorize_launch("AUTH-WRONG-0000-FAIL")
submarine.authorize_launch("XYZ-INVALID-9999-FAKE")

# 🚀 Try launching with a valid code
submarine.authorize_launch("AUTH-XYZ123-4567-SECURE")
