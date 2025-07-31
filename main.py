import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_async

app = FastAPI(title="Unow Mailer")

@app.get('/')
def index():
    return 'Hello World!'

@app.get('/send-email')
async def send_welcome_email():
    await send_email_async("Welcome Email", "qesantiago@gmail.com", "Welcome")
    return 'Success'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)