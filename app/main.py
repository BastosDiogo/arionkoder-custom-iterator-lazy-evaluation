from routes import payments
from version import __version__
from fastapi import FastAPI


app = FastAPI(
    title="Custom Iterator Lazy Evaluation",
    version=__version__,
    contact={
        "name": "Diogo Bastos",
        "url": "https://github.com/BastosDiogo",
        "email": "bmnetto.diogo@gmail.com",
    }
)

app.include_router(payments.router)