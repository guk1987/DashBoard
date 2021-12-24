from dotenv import load_dotenv
import os

load_dotenv()
mailid = os.environ.get("mailid")
mailpw = os.environ.get("mailpw")

print(mailid)
print(mailpw)
