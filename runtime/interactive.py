def start_session(agent_executor):
    print("\n🤖 Agent ready! Type a query")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("👉 Your query: ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            print("👋 Exiting... Goodbye!")
            break

        try:
            result = agent_executor.invoke({"input": query})
            print("\n--- Agent Output ---")
            print(result.get("output", result), "\n")
        except Exception as e:
            print(f"Error: {e}\n")
