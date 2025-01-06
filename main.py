from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()

from openai_client import generate

@app.post("/generate")
async def generate_reference(request: Request):
    try:
        form_data = await request.json()
        student_name = form_data.get('studentName')
        result = generate(NAME=student_name)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


