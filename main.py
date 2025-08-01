import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_async
from pydantic import BaseModel

app = FastAPI(title="Unow Mailer")

@app.get('/')
def index():
    return 'healthy'

class Info(BaseModel):
    email: str
    subject: str
    message: str

@app.post('/send-email')
async def send_welcome_email(info: Info):
    await send_email_async(info.subject, info.email, info.message)
    return 'Success'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)