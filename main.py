from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello FastAPI"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, # 코드변경시 서버에 바로 적용
                host="0.0.0.0",          # 0.0.0.0 외부 접속 허용
                port=8000)               # 서버 포트를 8000번 사용 
                                         # (포트 바꾸면 ec2 인바운드 규칙 고려 포트 열어놓기)