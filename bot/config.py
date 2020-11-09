import os
import json
from distutils.util import strtobool as stb

# --------------------------------------
BOT_TOKEN = "1423708014:AAF44OnMGxWkxHQGsThvDDUe6VIC_AUdIQA"
GDRIVE_FOLDER_ID = "1awz8PcWb1QDeB-eHhDClCSjzHl7EooMO"
# Default folder id.
OWNER_ID = 1032969693
# Example: OWNER_ID = 619418070
AUTHORISED_USERS = [907994231,760135118]
# Example: AUTHORISED_USERS = [63055333, 100483029, -1003943959]
INDEX_URL = ""
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = False
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
