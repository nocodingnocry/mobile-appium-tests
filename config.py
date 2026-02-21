from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class TestUser:
    login: str
    password: str


class TestUsers:
    STANDARD_USER = TestUser(
        login = os.getenv('STANDART_USER'),
        password = os.getenv('STANDART_PASSWORD')
    )

    LOCKED_USER = TestUser(
        login = os.getenv('LOCKED_OUT_USER'),
        password = os.getenv('LOCKED_USER_PASSWORD')
    )

    PROBLEM_USER = TestUser(
        login = os.getenv('PROBLEM_USER'),
        password = os.getenv('PROBLEM_USER_PASSWORD')
    )