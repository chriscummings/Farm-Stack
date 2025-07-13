"""
Docker Entry
================================================================================

"""

import os
#
import uvicorn


LOG_LEVEL = os.environ["LOG_LEVEL"]

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", log_level=LOG_LEVEL)
