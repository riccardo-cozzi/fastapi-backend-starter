from fastapi import FastAPI
import uvicorn
from model import EmailModel
from email_manager import send
import dataloader

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/send-email/")
def email_endpoint(email: EmailModel):
    try: 
        print(f"Sending mail to '{email.to}' with subject '{email.subject}'...")
        send(email)
        return {"status": 200, "detail": "email sent."}
    except Exception as e: 
        print("Error: ", str(e))
        return {"status": 500, "error": "internal", "detail": str(e)}

 
@app.post("/get-users/")
def get_users():
    return dataloader.load_users()

    


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)