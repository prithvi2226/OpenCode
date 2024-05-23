# screenshot-to-code

A simple tool to convert screenshots, mockups and Figma designs into clean, functional code using AI. **Now supporting GPT-4O!**

https://github.com/abi/screenshot-to-code/assets/23818/6cebadae-2fe3-4986-ac6a-8fb9db030045

Supported stacks:

- HTML + Tailwind
- React + Tailwind
- Vue + Tailwind
- Bootstrap
- Ionic + Tailwind
- SVG

Supported AI models:

- GPT-4O - Best model!
- GPT-4 Turbo (Apr 2024)
- GPT-4 Vision (Nov 2023)
- Claude 3 Sonnet
- DALL-E 3 for image generation

See the [Examples](#-examples) section below for more demos.

We also just added experimental support for taking a video/screen recording of a website in action and turning that into a functional prototype. 

![google in app quick 3](https://github.com/abi/screenshot-to-code/assets/23818/8758ffa4-9483-4b9b-bb66-abd6d1594c33)

[Learn more about video here](https://github.com/abi/screenshot-to-code/wiki/Screen-Recording-to-Code).

[Follow me on Twitter for updates](https://twitter.com/_abi_).

## 🚀 Try It Out without no install

[Try it live on the hosted version (paid)](https://screenshottocode.com).

## 🛠 Getting Started

The app has a React/Vite frontend and a FastAPI backend. You will need an OpenAI API key with access to the GPT-4 Vision API or an Anthropic key if you want to use Claude Sonnet, or for experimental video support.

Run the backend (I use Poetry for package management - `pip install poetry` if you don't have it):

```bash
cd backend
echo "OPENAI_API_KEY=sk-your-key" > .env
poetry install
poetry shell
poetry run uvicorn main:app --reload --port 7001
```

If you want to use Anthropic, add the `ANTHROPIC_API_KEY` to `backend/.env` with your API key from Anthropic.

Run the frontend:

```bash
cd frontend
yarn
yarn dev
```

Open http://localhost:5173 to use the app.

If you prefer to run the backend on a different port, update VITE_WS_BACKEND_URL in `frontend/.env.local`

For debugging purposes, if you don't want to waste GPT4-Vision credits, you can run the backend in mock mode (which streams a pre-recorded response):

```bash
MOCK=true poetry run uvicorn main:app --reload --port 7001
```

## Docker

If you have Docker installed on your system, in the root directory, run:

```bash
echo "OPENAI_API_KEY=sk-your-key" > .env
docker-compose up -d --build
```

The app will be up and running at http://localhost:5173. Note that you can't develop the application with this setup as the file changes won't trigger a rebuild.
