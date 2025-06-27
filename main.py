import os, time
from instagrapi import Client

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
SESSION_ID = os.getenv("IG_SESSION_ID")  # Optional
PFP_DIR = "pfps"
DELAY = 3

def login():
    cl = Client()
    if SESSION_ID:
        cl.login_by_sessionid(SESSION_ID)
        print("✅ Logged in using session ID")
    else:
        cl.login(USERNAME, PASSWORD)
        print("✅ Logged in using username/password")
    return cl

def main():
    cl = login()
    pfp_files = sorted([
        os.path.join(PFP_DIR, f)
        for f in os.listdir(PFP_DIR)
        if f.lower().endswith((".jpg", ".png"))
    ])
    while True:
        for file in pfp_files:
            try:
                with open(file, "rb") as f:
                    cl.account_change_profile_picture(f.read())
                print(f"✅ Changed PFP to {file}")
            except Exception as e:
                print(f"❌ Error with {file}: {e}")
            time.sleep(DELAY)

if __name__ == "__main__":
    main()
  
