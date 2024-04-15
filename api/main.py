from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.User import User
from models.Feedback import Feedback
from models.Product import Product
from typing import List
import schema
from fastapi.responses import RedirectResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# App code for creating routes here