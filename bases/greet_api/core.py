
from fastapi import FastAPI, Query

from bases.bank.bankactions import BankActions
from components.log.core import get_logger

logger = get_logger("greet-FastAPI-logger")
app = FastAPI()

@app.get("/")
def root(name: str = Query(..., description="Enter your name")) -> dict:
    logger.info("The FastAPI root endpoint was called with name: %s", name)

    # Initialize the BankActions object with the provided name
    bank_user = BankActions(name)
    balance_info = bank_user.check_balance()

    # Return the desired message
    return {
        "message": "Hello, world!",  # Replace with `message.hello_world()` if defined elsewhere
        "balance_info": balance_info
    }
