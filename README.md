# 📱 Thinking Sky: Connect With Anyone, Anywhere! 🌍

Welcome to our ChatApp, a dynamic platform built with Python and React (JavaScript) that allows users to interact publicly. With this app, anyone can connect with anyone else, making the world a smaller, more accessible place. 🚀 Plus, it's not just about text; you can also send images, files, and more to keep the conversation going. 📸📁

## Prerequisites 📋

Before diving into the world of endless chatting, make sure you have these tools ready on your machine:

- Python 3.6+
- Node.js
- vite js
- npm (usually comes with Node.js)

## Getting Started 🚀
## 📦 Installation


1. **Clone the Repo**: First up, grab a copy of our codebase by cloning this repo to your local machine.

```bash
git clone https://github.com/siddhu1919/Thinking-Sky_chatapp--Py-Js-.git
cd Thinking-Sky_chatapp--Py-Js-
```
2. **Navigate Through Folders**: You'll find two main directories:
   - `backend`
   - `frontend`

### Setting Up the Backend 🛠️

1. **Jump into the Backend**: Navigate to the `backend` folder.
   
![image](https://github.com/siddhu1919/Thinking-Sky_chatapp--Py-Js-/assets/85176765/6aa256f0-218b-410b-bd6c-048ed0688487)

2. **Virtual Environment**: Set up a Python virtual environment to keep things tidy.
![image](https://github.com/siddhu1919/Thinking-Sky_chatapp--Py-Js-/assets/85176765/5bad9fe0-0638-4e35-9678-b794fce1611d)

3. **Install Requirements**: Install the Python requirements to get all the necessary packages.
 
```bash
pip install -r requirements.txt
```

4. **Fire Up the Server**: Open a new PowerShell/CMD window in your IDE (VSCode recommended) and launch the server with:

```bash
uvicorn main:app --reload --port 3001
```

5. **Connect to Chat Engine**: Head over to `main.py` to connect our backend to the Chat Engine.
- Create a **PRIVATE_KEY** by signing up for a free account at [ChatEngine.io](https://chatengine.io/).
- Create a project, go to its settings, and copy your Private Key.
- ![image](https://github.com/siddhu1919/Thinking-Sky_chatapp--Py-Js-/assets/85176765/bfbcbc07-0632-4f9f-bd83-9756f346bf2f)
- ![image](https://github.com/siddhu1919/Thinking-Sky_chatapp--Py-Js-/assets/85176765/09db329c-9196-41a8-9f83-7e350fa4b13a)


### Setting Up the Frontend 🎨

1. **Connect to Chat Engine**: All we need here is to add our Project ID as `VITE_CHAT_ENGINE_PROJECT_ID` within `frontend/.env.local`.
- ![image](https://github.com/siddhu1919/Thinking-Sky_chatapp--Py-Js-/assets/85176765/7292f686-62e6-47a8-8ffb-fbf6b64d1743)

2. **Create `.env.local` File**: Within the `frontend` directory, create a `.env.local` file and populate it with your project ID like so:
(Replace `...` with your actual project ID).

3. **Run the App**: With everything in place, run the following command in a new terminal window:
   
```bash
npm run dev
```

And that's it! Your app should now be up and running! 🎉🎉🎉

## Dive In! 🌊

Now that you've got everything set up, it's time to dive in and start connecting with people from all around the globe. Whether it's text, images, or files, Thinking Sky brings everyone closer together. Enjoy exploring this space where anyone can connect with anyone. Happy chatting! 💬🌐
