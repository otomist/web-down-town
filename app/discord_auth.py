import os
import requests
from dotenv import load_dotenv
from fastapi import APIRouter

router = APIRouter()

load_dotenv("../.env")

API_ENDPOINT = os.getenv("API_ENDPOINT")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

if not all([API_ENDPOINT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI]):
    raise ValueError("Missing environment variables")


def exchange_code(code: str):
    if CLIENT_ID and CLIENT_SECRET:
        r = requests.post(
            url=f"{API_ENDPOINT}/oauth2/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            auth=(CLIENT_ID, CLIENT_SECRET),
        )
        r.raise_for_status()
        return r.json()
    else:
        raise ValueError("Missing client_id or client_secret")


@router.get("/api/discord/auth", tags=["discord"])
async def discord_auth(code: str):
    response = exchange_code(code)
    return response
