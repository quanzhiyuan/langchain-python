#!/usr/bin/env python
import sys
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_MODEL

# 设置详细的日志记录
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI(
    model=OPENAI_MODEL,
    openai_api_base=OPENAI_API_BASE,
    openai_api_key=OPENAI_API_KEY,
)


# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 添加更详细的错误处理
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("An error occurred:", exc_info=True)
    error_info = {
        "error_type": type(exc).__name__,
        "error_message": str(exc),
        "traceback": traceback.format_exc()
    }
    logger.error(f"Detailed error info: {error_info}")
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred.", "detail": error_info},
    )

# 添加一个测试路由
@app.get("/test")
async def test_route():
    return {"message": "Test route is working"}

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn
    
    # 添加异常处理
    try:
        uvicorn.run(app, host="localhost", port=8000, log_level="debug")
    except Exception as e:
        logger.critical(f"Failed to start server: {e}", exc_info=True)
        sys.exit(1)