# Long-Running Backend Servers

Run a real server process (FastAPI, Express, Flask, etc.) alongside the site during development. Use this when you need:

- WebSocket or SSE streaming
- In-memory state across requests
- Framework features (middleware, dependency injection, ORMs)
- Background tasks or scheduled work
- Multiple related endpoints with shared state
- LLM or media generation (text, image, video, audio) — **read `shared/20-llm-api.md`** for SDKs, models, and helper scripts

## How It Works

1. Write a server that listens on a port (for example `8000`)
2. Start it yourself from the project directory with the repo's normal runner (`python`, `uvicorn`, `node`, `npm run dev`, etc.)
3. Point the frontend at an explicit base URL during local development, usually `http://localhost:8000`
4. Treat preview and deployment routing as project-specific configuration. This shared file does not assume an automatic port proxy or placeholder replacement.

## Visitor Data Isolation

If the site stores visitor-created or per-session data, make that boundary explicit in your own auth or session layer. Use signed session identifiers, auth tokens, or another server-side visitor key that you control. Do not assume the runtime injects special visitor headers for you.

Read-only content authored at build time usually does not need per-visitor scoping.

## Step-by-Step

### 1. Write the Server

Create a standard server in your project directory. Example with FastAPI:

```python
#!/usr/bin/env python3
"""api_server.py — runs on port 8000 inside the sandbox."""
import sqlite3
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

db = sqlite3.connect("data.db", check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

@asynccontextmanager
async def lifespan(app):
    yield
    db.close()

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Item(BaseModel):
    name: str

@app.get("/api/items")
def list_items():
    rows = db.execute("SELECT id, name, created_at FROM items ORDER BY id").fetchall()
    return [{"id": r[0], "name": r[1], "created_at": r[2]} for r in rows]

@app.post("/api/items", status_code=201)
def create_item(item: Item):
    cur = db.execute("INSERT INTO items (name) VALUES (?)", [item.name])
    db.commit()
    return {"id": cur.lastrowid, "name": item.name}

@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    db.execute("DELETE FROM items WHERE id = ?", [item_id])
    db.commit()
    return {"deleted": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 2. Start the Server

Start the backend with a normal shell command from the project directory. Keep the command in `package.json`, a Make target, or another checked-in script so the launch path stays repeatable.

```bash
python api_server.py
```

If you prefer live reload, use the framework's normal dev entrypoint instead (for example `uvicorn api_server:app --reload --host 0.0.0.0 --port 8000` or `node server.js`).

If the server calls LLM or media APIs, provide credentials through environment variables or whatever secret mechanism the current runtime supports. This shared file does not assume automatic credential injection. **Read `shared/20-llm-api.md`** for SDK details and helper scripts.

Fail fast on missing configuration at process startup rather than on the first user request.

If the site can trigger paid APIs or external systems, make the billing and sharing risk explicit in the product behavior and project handoff. Public traffic turns every request into real spend or real side effects.

### 3. Connect the Frontend

Keep the API base URL configurable instead of scattering backend origins through the codebase.

```js
const API = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function loadItems() {
  const res = await fetch(`${API}/api/items`);
  return res.json();
}

async function addItem(name) {
  const res = await fetch(`${API}/api/items`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
  return res.json();
}
```

### 4. Preview and Deployment

This shared reference does not prescribe a deployment command or a built-in backend proxy. When moving beyond local development, document three things explicitly:

- where the backend runs
- which base URL the frontend should call
- how secrets are provisioned in that environment

Prefer one config surface such as `VITE_API_BASE_URL` and `VITE_WS_URL` rather than placeholder strings spread throughout the app.

## WebSocket Example

Server (Python with websockets):

```python
#!/usr/bin/env python3
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"echo: {message}")

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8000):
        await asyncio.Future()

asyncio.run(main())
```

Client:

```js
const WS_URL = import.meta.env.VITE_WS_URL ?? "ws://localhost:8000/ws";
const ws = new WebSocket(WS_URL);
```

Keep the WebSocket URL configurable for the target runtime instead of deriving it from special placeholder paths.

## Express.js Example

```js
// server.js
const express = require("express");
const app = express();
app.use(express.json());

let items = [];
let nextId = 1;

app.get("/api/items", (req, res) => res.json(items));
app.post("/api/items", (req, res) => {
  const item = { id: nextId++, ...req.body };
  items.push(item);
  res.status(201).json(item);
});

app.listen(8000, "0.0.0.0", () => console.log("listening on 8000"));
```

```bash
node server.js
```

## Multiple Ports

You can run multiple servers on different ports. Keep each one configurable:

```js
const API = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";
const WS_URL = import.meta.env.VITE_WS_URL ?? "ws://localhost:8001/ws";
```

## Limits and Guardrails

- Bind to `0.0.0.0` if the server must be reachable outside the current process or container boundary; use `localhost` only for same-machine-only testing
- Use `4xx` for caller errors and `5xx` for real server faults
- Make request-size limits and timeouts explicit in framework config
- SSE and WebSocket endpoints need heartbeat or keepalive behavior if you expect long-lived connections
- Do not hide infrastructure assumptions in magic path placeholders; keep base URLs configurable