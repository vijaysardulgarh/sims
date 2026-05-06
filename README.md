md sims

cd sims

md backend
md frontend

cd backend

python -m pip install --upgrade pip

python -m venv venv

venv\scripts\activate

pip install django

Create a .gitignore File

          # Python/Django
          venv/
          env/
          *.pyc
          __pycache__/
          db.sqlite3
          *.media/
          .env
          
          # Frontend (React/Vue/etc.)
          node_modules/
          dist/
          build/    

git init          

git remote add origin https://github.com/vijaysardulgarh/sims.git

git push -u origin main

django-admin startproject sims .

Commands for pushing files to github

          git status
          git add .
          git commit -m "Added new feature"
          git push



Creating Frontend

    cd frontend
    npm create vite@latest
    npm install
    npm run dev

npm install react-router-dom axios
npm install tailwindcss @tailwindcss/vite


vite.config.js

import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)



src/index.css

    Remove Everything and add 
    import './index.css'


src/main.jsx

Make sure this exists:

import './index.css'

src/App.jsx

  replace with

  export default function App() {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <h1 className="text-5xl font-bold text-blue-600">
          SIMS Frontend
        </h1>
      </div>
    )
  }

  npm run dev
  http://localhost:5173