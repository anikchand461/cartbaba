# 🛒 CartBaba — AI-Powered E-commerce Search Assistant

CartBaba is an **agentic AI shopping assistant** that understands natural language queries and returns **smart, ranked product recommendations** using a multi-agent system.

Instead of keyword search, users can ask:

```text
"shoes for men under 5000"
"bags for ladies"
"gaming headphones under 3000"
```

…and CartBaba intelligently handles the rest.

---

# 🚀 Features

- 🧠 **Natural Language Search** (no filters needed)
- 🤖 **Multi-Agent Architecture (CrewAI)**
- ⚡ **Fast LLM inference via Groq**
- 📊 **ML-based Product Ranking (semantic similarity + rating)**
- 🔄 **Dynamic Product Fetching (API + fallback system)**
- 🎯 **Intent Extraction (category, price, use-case)**
- 🖥️ **Clean Vanilla JS Frontend**

---

# 🧠 System Architecture

```text
User Query
   ↓
🧠 Intent Agent
   ↓
🧰 Tool Selection Agent
   ↓
🔎 Search Agent (API + fallback)
   ↓
🧹 Review Agent
   ↓
📊 Ranking Agent (Embeddings + Scoring)
   ↓
🤖 Final Output Agent
   ↓
Frontend UI
```

---

# 🤖 Agents Used

| Agent         | Role                      |
| ------------- | ------------------------- |
| Intent Agent  | Extracts structured query |
| Tool Agent    | Decides data source       |
| Search Agent  | Fetches product data      |
| Review Agent  | Filters irrelevant items  |
| Ranking Agent | Scores products           |
| Final Agent   | Generates explanation     |

---

# ⚙️ Tech Stack

### Backend

- FastAPI
- CrewAI
- Groq
- Sentence Transformers

### Frontend

- HTML, CSS, Vanilla JavaScript

### ML / AI

- Embeddings: `all-MiniLM-L6-v2`
- Ranking: cosine similarity + rating score

---

# 📦 Installation

## 1. Clone repo

```bash
git clone https://github.com/your-username/cartbaba.git
cd cartbaba/backend
```

---

## 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup environment variables

Create `.env` inside `backend/`

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5. Run backend

```bash
uvicorn app.main:app --reload
```

---

## 6. Run frontend

Open:

```text
frontend/index.html
```

---

# 🔍 Example Queries

- shoes under 5000
- bags for women
- gaming mouse under 2000
- formal shoes for office

---

# 🧪 How It Works

### 1. Intent Extraction

LLM converts:

```text
"shoes under 5000"
```

into:

```json
{
  "category": "shoes",
  "max_price": 5000
}
```

---

### 2. Product Fetching

- Uses `dummyjson` API
- Falls back to dynamic fake data if no results

---

### 3. Ranking

```text
Score = 0.7 * semantic_similarity + 0.3 * rating
```

---

### 4. Final Output

- Ranked product list
- AI-generated explanation

---

# ⚠️ Current Limitations

- Uses fake/dummy API (not real marketplaces)
- Limited product categories
- No user personalization yet

---

# 🚀 Future Improvements

- 🔗 Integrate real APIs (eBay, Amazon alternatives)
- 🧠 Add user memory (preferences)
- 🖼️ Improve UI (product images, filters)
- 📦 Add cart + checkout simulation
- ⚡ Optimize ranking with more features (price sensitivity, brand)

---

# 🏆 Why This Project Stands Out

- Not just an LLM wrapper ❌
- Full **agentic system design** ✅
- Combines:
  - LLM reasoning
  - ML ranking
  - API integration
  - Frontend UI

---

# 👨‍💻 Author

**Anik Chand**

---

# ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!

---

# 🔥 One-line Summary

> CartBaba turns natural language into intelligent shopping decisions using AI agents.
