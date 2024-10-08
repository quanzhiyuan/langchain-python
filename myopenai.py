# 导入必要的库
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_MODEL
import logging

logging.info('infor:', OPENAI_API_KEY)
# 检查 API 密钥是否设置
if not OPENAI_API_KEY or OPENAI_API_KEY == "your_api_key_here":
    raise ValueError("请在 config.py 文件中设置您的 OPENAI_API_KEY。您需要购买自己的 OpenAI API 密钥。")

# 系统提示模板
sys_template = "Translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages([("system", sys_template), ("user", "{text}")])

# 初始化 ChatOpenAI 实例
llm = ChatOpenAI(
    model=OPENAI_MODEL,
    openai_api_base=OPENAI_API_BASE,
    openai_api_key=OPENAI_API_KEY,
)

# 初始化字符串输出解析器
parser = StrOutputParser()

# 创建链
chain = prompt | llm | parser

# 向 LLM 发送请求并获取响应
res = chain.invoke({"language": "Chinese", "text": "Hello, world!"})

# 打印解析后的消息
print(res)