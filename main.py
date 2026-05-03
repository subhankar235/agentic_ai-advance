from agent import run_agent

print("AI Agent Started...")

while True:
    user = input("You: ")

    if user == "exit":
        break

    if user.strip() == "":
        continue

    answer = run_agent(user)
    print("Agent:", answer)