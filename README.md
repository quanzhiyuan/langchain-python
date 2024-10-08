# LangChain Python 项目

这是一个基于 LangChain 和 OpenAI API 的 Python 项目，提供了简单易用的接口来与各种 AI 模型进行交互。

## 功能

- 与 GPT 模型进行文本对话
- 生成图像（使用 DALL-E 模型）
- 分析和处理自然语言
- 自定义 API 调用参数
- 使用 LangChain 进行高级语言处理任务

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/quanzhiyuan/langchain-python.git
   cd langchain-python
   ```

2. 安装所需的依赖：
   ```
   pip install -r requirements.txt
   ```

3. 设置 OpenAI API 密钥：
   将您的 OpenAI API 密钥添加到环境变量中或创建一个 `.env` 文件：
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 配置

1. 复制 `config.py.example` 文件并重命名为 `config.py`：
   ```
   cp config.py.example config.py
   ```

2. 在 `config.py` 文件中设置您的 OpenAI API 密钥和其他配置：
   ```python
   OPENAI_API_KEY = "your_api_key_here"
   OPENAI_API_BASE = "https://api.openai.com/v1"  # 或其他自定义 API 基础 URL
   ```

3. 确保 `config.py` 文件已添加到 `.gitignore` 中，以避免将敏感信息提交到版本控制系统。

注意：您需要购买自己的 OpenAI API 密钥才能使用此项目。请访问 [OpenAI 官网](https://openai.com/) 了解如何获取 API 密钥。

## 使用方法

在设置好配置文件后，您可以运行 `myopenai.py` 来测试基本功能：

## 配置

您可以通过修改相关配置文件来自定义项目行为，例如更改模型、调整参数等。

## 贡献

欢迎贡献代码、报告问题或提出新功能建议。请遵循以下步骤：

1. Fork 该仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证

该项目使用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件

## 联系方式

Quan Zhiyuan - [@quanzhiyuan](https://github.com/quanzhiyuan)

项目链接: [https://github.com/quanzhiyuan/langchain-python](https://github.com/quanzhiyuan/langchain-python)