import sys
import asyncio

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import threading
import uvicorn
import os
import logging
logging.getLogger("asyncio").setLevel(logging.CRITICAL)

from fastapi import FastAPI
from app.apis.routes import router

app = FastAPI()
app.include_router(router=router, prefix="/api/v1")

def run_fastapi():
    uvicorn.run(app=app, host="0.0.0.0", port=8000,
                loop="asyncio", lifespan="off")

if __name__ == "__main__":
    t1 = threading.Thread(target=run_fastapi, daemon=True)
    t1.start()

    # Run streamlit directly in main process — no subprocess
    from streamlit.web import cli as stcli
    sys.argv = [
        "streamlit", "run", "streamlit_ui.py",
        "--server.port=7860",
        "--server.address=0.0.0.0",
        "--server.headless=true"
    ]
    stcli.main()