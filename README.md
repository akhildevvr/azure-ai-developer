# Azure AI Developer - Hands-On Workshop

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/akhildevvr/azure-ai-developer)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Azure AI](https://img.shields.io/badge/Azure-AI%20Foundry-0078D4?logo=microsoft-azure)](https://ai.azure.com/)
[![Semantic Kernel](https://img.shields.io/badge/Semantic-Kernel-purple)](https://learn.microsoft.com/en-us/semantic-kernel/)

## 🚀 Overview

Welcome to the **Azure AI Developer Workshop**! This hands-on workshop provides a comprehensive introduction to building AI-powered applications using **Azure AI Foundry** and **Semantic Kernel**. Whether you're new to OpenAI or an experienced developer looking to integrate AI into your applications, this workshop will guide you through the essential concepts and practical implementations.

This repository contains materials for a structured learning experience designed to be completed as a team-based activity, with each challenge taking between 30-90 minutes.

## ✨ What You'll Learn

Through a series of progressive challenges, you'll gain practical experience in:

- 🤖 **Building AI Chat Applications** - Create conversational AI using Semantic Kernel and Python
- 🔌 **Creating and Using Plugins** - Extend AI capabilities with custom plugins and enable automatic function calling
- 🌐 **API Integration** - Import and use existing APIs through OpenAPI specifications
- 📚 **Retrieval Augmented Generation (RAG)** - Implement document chunking, embeddings, and AI grounding techniques
- 🎨 **Image Generation** - Work with DALL-E for text-to-image generation
- 🛡️ **Responsible AI** - Configure and test content filters in Azure AI Foundry
- 🤝 **Multi-Agent Systems** - Build sophisticated multi-agent conversational workflows

## 📋 Prerequisites

Before starting this workshop, ensure you have:

- **Azure Subscription** - Access to Azure with permissions to create resources
- **Python 3.8+** - Installed on your local machine
- **Visual Studio Code** - With the Python extension installed
- **Git** - For cloning this repository
- **Basic Python Knowledge** - Familiarity with Python programming

### Optional but Recommended
- **GitHub Copilot** - Enhanced coding experience (free trial available)
- **Azure AI Foundry Access** - Active Azure AI Foundry project

## 🏁 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/akhildevvr/azure-ai-developer.git
cd azure-ai-developer
```

### 2. Set Up Your Development Environment

Navigate to the Python workshop directory:

```bash
cd Python
```

### 3. Install Dependencies

Create a virtual environment and install required packages:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
cd src
pip install -r requirements.txt
```

### 4. Configure Azure AI Foundry

Create a `.env` file in the `src` directory with your Azure AI Foundry credentials:

```env
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your-deployment-name"
AZURE_OPENAI_ENDPOINT="your-endpoint-url"
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_API_VERSION="your-api-version"
```

### 5. Start Learning!

Begin with [Challenge 00](./Python/challenges/Challenge-00.md) to verify your setup and then progress through the workshop.

## 📚 Workshop Structure

The workshop consists of **8 progressive challenges**, each building upon the previous one:

| Challenge | Topic | Key Concepts |
|-----------|-------|-------------|
| [**00**](./Python/challenges/Challenge-00.md) | **Prerequisites** | Environment setup, tool installation |
| [**01**](./Python/challenges/Challenge-01.md) | **Azure AI Foundry Fundamentals** | Model deployment, prompt engineering |
| [**02**](./Python/challenges/Challenge-02.md) | **Semantic Kernel Fundamentals** | SDK basics, chat implementation |
| [**03**](./Python/challenges/Challenge-03.md) | **Plugins** | Custom functions, auto function calling |
| [**04**](./Python/challenges/Challenge-04.md) | **OpenAPI Integration** | Importing APIs, OpenAPI specifications |
| [**05**](./Python/challenges/Challenge-05.md) | **RAG Pattern** | Document chunking, embeddings, Azure AI Search |
| [**06**](./Python/challenges/Challenge-06.md) | **Responsible AI** | Content filters, safety configurations |
| [**07**](./Python/challenges/Challenge-07.md) | **Image Generation** | DALL-E integration, image plugins |
| [**08**](./Python/challenges/Challenge-08.md) | **Multi-Agent Systems** | Agent orchestration, complex workflows |

## 🎯 Who Is This For?

This workshop is ideal for:

- **Developers** looking to integrate AI into their applications
- **Teams** wanting to upskill in Azure AI technologies
- **Students** learning about modern AI development practices
- **Technical Leaders** exploring AI implementation strategies

### Recommended Approach

- **Team Size**: 3-5 people per group
- **Time Commitment**: 4-12 hours (depending on experience level)
- **Format**: Hands-on, challenge-based learning with research encouraged

## 🛠️ Technology Stack

- **Azure AI Foundry** - AI model deployment and management
- **Semantic Kernel** - AI orchestration SDK
- **Python** - Primary programming language
- **Streamlit** - Web application framework
- **Azure AI Search** - Vector search and RAG implementation
- **OpenAI Models** - GPT-4, GPT-3.5, DALL-E, text-embedding-ada-002

## 📖 Additional Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-services/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [Semantic Kernel Blog](https://devblogs.microsoft.com/semantic-kernel/)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)




## 🌟 Acknowledgments

Special thanks to the Microsoft Azure AI and Semantic Kernel teams for providing the foundational technologies and documentation that make this workshop possible.

## 💡 Support

If you encounter issues or have questions:

1. Review the challenge-specific documentation in the [Python/challenges](./Python/challenges/) directory
2. Check the [Python README](./Python/README.md) for detailed information
3. Consult the official [Semantic Kernel documentation](https://learn.microsoft.com/semantic-kernel/)
4. Open an issue in this repository

---

**Ready to start?** Head over to [Challenge 00](./Python/challenges/Challenge-00.md) to begin your AI development journey! 🚀
