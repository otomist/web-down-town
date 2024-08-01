import os
import requests
from dotenv import load_dotenv
from fastapi import APIRouter

router = APIRouter()

load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

if not all([API_ENDPOINT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI]):
    raise ValueError("Missing environment variables")


def exchange_code(code):
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    post_url = f"{API_ENDPOINT}/oauth2/token"
    r = requests.post(
        post_url,
        data=data,
        headers=headers,
        auth=(CLIENT_ID, CLIENT_SECRET),  # type: ignore
    )
    r.raise_for_status()
    return r.json()


@router.get("/discord/", tags=["discord"])
async def read_item():
    return {"message": "Hello World"}
