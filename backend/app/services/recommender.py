from crewai import Task, Crew
import json

# Agents
from app.agents.intent_agent import intent_agent
from app.agents.tool_agent import tool_agent
from app.agents.review_agent import review_agent
from app.agents.final_agent import final_agent

# LLM (native crewai)
from app.core.llm import get_llm

# Core logic
from app.agents.search_agent import search_products
from app.agents.ranking_agent import rank_products


# -----------------------------
# 🧠 Helper: safe JSON parser
# -----------------------------
def safe_json_loads(text):
    try:
        return json.loads(text)
    except:
        return {}


def run_cartbaba(query: str):

    # =========================
    # 🧠 1. INTENT AGENT (Mixtral)
    # =========================
    intent_task = Task(
        description=f"""
        Extract structured shopping intent from:

        {query}

        Return ONLY JSON:
        {{
          "category": "",
          "max_price": null,
          "gender": "",
          "use_case": ""
        }}
        """,
        agent=intent_agent,
        expected_output="Strict JSON with category, max_price, gender, use_case"
    )

    # =========================
    # 🧰 2. TOOL SELECTION
    # =========================
    tool_task = Task(
        description=f"""
        Decide best data source for:

        {query}

        Options:
        - API
        - SCRAPE

        Return ONLY one word.
        """,
        agent=tool_agent,
        expected_output="Either API or SCRAPE"
    )

    # =========================
    # 🧹 3. REVIEW TASK
    # =========================
    review_task = Task(
        description="""
        Filter products:
        - remove irrelevant items
        - remove low rating (<3.5)
        - keep only best matches

        Return ONLY JSON list.
        """,
        agent=review_agent,
        expected_output="Filtered JSON product list"
    )

    # =========================
    # 🧠 4. FINAL OUTPUT
    # =========================
    final_task = Task(
        description="""
        Generate final recommendation:
        - explain top products
        - be concise
        """,
        agent=final_agent,
        expected_output="User-friendly explanation"
    )

    # =========================
    # 🎯 5. CREW EXECUTION
    # =========================
    crew = Crew(
        agents=[
            intent_agent,
            tool_agent,
            review_agent,
            final_agent
        ],
        tasks=[
            intent_task,
            tool_task,
            review_task,
            final_task
        ],
        verbose=True
    )

    result = crew.kickoff()

    # =========================
    # 🧠 6. PARSE INTENT
    # =========================
    intent_data = safe_json_loads(str(result.tasks_output[0]))

    category = intent_data.get("category", "shoes")

    # =========================
    # 🔎 7. FETCH PRODUCTS
    # =========================
    products = search_products({
        "category": category
    })

    # =========================
    # 📊 8. RANK PRODUCTS
    # =========================
    ranked_products = rank_products(products, query)

    # =========================
    # 📦 FINAL RESPONSE
    # =========================
    return {
        "query": query,
        "intent": intent_data,
        "products": ranked_products,
        "final": str(result.tasks_output[-1])
    }
