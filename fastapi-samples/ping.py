from fastapi import FastAPI
app = FastAPI(title="Ping Example")

@app.get('/ping')
def ping():
  return {"pong": true}
