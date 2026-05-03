# agent.py

from llm import call_llm
from tools import read_file
from memory import add_message, get_history


def run_agent(user_input):

    # 🟢 Step 1: Save user message
    add_message("user", user_input)

    # 🧠 Step 2: Build messages
    messages = [
        {
            "role": "system",
            "content": """
            You are an AI agent.

            If the user mentions any file (.txt),
            you MUST respond ONLY like:

            TOOL: read_file(filename)

            Do NOT answer directly.
            Do NOT summarize yourself.
            ONLY call the tool.
            """
        }
    ] + get_history()

    # 🧠 Step 3: Ask LLM what to do
    reply = call_llm(messages)

    print("LLM reply:", reply)   # 🔥 DEBUG (important)

    # 🔧 Step 4: Tool execution
    if reply.startswith("TOOL:"):
        tool_call = reply.replace("TOOL:", "").strip()

        if tool_call.startswith("read_file"):
            filename = tool_call.split("(")[1].split(")")[0].replace('"', '')

            # 🛠️ Run tool
            file_data = read_file(filename)

            # 🧠 Step 5: Summarize using LLM
            summary = call_llm([
                {"role": "user", "content": f"Summarize this:\n{file_data}"}
            ])

            add_message("assistant", summary)
            return summary

    # 🟡 Step 6: Normal response
    add_message("assistant", reply)
    return reply