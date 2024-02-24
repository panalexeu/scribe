from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get('/health-check')
async def health_check():
    return {'status': 'healthy'}


handler = Mangum(app)
