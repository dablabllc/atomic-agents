import os
import instructor
import openai
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from atomic_agents.lib.components.agent_memory import AgentMemory
from atomic_agents.agents.base_agent import BaseAgent, BaseAgentConfig, BaseAgentInputSchema, BaseAgentOutputSchema

from dotenv import load_dotenv
from quickstart.config import get_base_url, get_api_key, get_fast_llm


# Initialize a Rich Console for pretty console outputs
console = Console()

# Memory setup
memory = AgentMemory()

# Initialize memory with an initial message from the assistant
initial_message = BaseAgentOutputSchema(chat_message="Hello! How can I assist you today?")
memory.add_message("assistant", initial_message)

# OpenAI client setup using the Instructor library for async operations
client = instructor.from_openai(openai.AsyncOpenAI(base_url=get_base_url(), api_key=get_api_key()), mode=instructor.Mode.JSON)

# Agent setup with specified configuration
agent = BaseAgent(
    config=BaseAgentConfig(
        client=client,
        model=get_fast_llm(),
        memory=memory,
    )
)

# Generate the default system prompt for the agent
default_system_prompt = agent.system_prompt_generator.generate_prompt()
# Display the system prompt in a styled panel
console.print(Panel(default_system_prompt, width=console.width, style="bold cyan"), style="bold cyan")

# Display the initial message from the assistant
console.print(Text("Agent:", style="bold green"), end=" ")
console.print(Text(initial_message.chat_message, style="green"))


async def main():
    # Start an infinite loop to handle user inputs and agent responses
    while True:
        # Prompt the user for input with a styled prompt
        user_input = console.input("\n[bold blue]You:[/bold blue] ")
        # Check if the user wants to exit the chat
        if user_input.lower() in ["/exit", "/quit"]:
            console.print("Exiting chat...")
            break

        # Process the user's input through the agent and get the streaming response
        input_schema = BaseAgentInputSchema(chat_message=user_input)
        console.print()  # Add newline before response

        # Use Live display to show streaming response
        with Live("", refresh_per_second=10, auto_refresh=True) as live:
            current_response = ""
            async for partial_response in agent.run_async(input_schema):
                if hasattr(partial_response, "chat_message") and partial_response.chat_message:
                    # Only update if we have new content
                    if partial_response.chat_message != current_response:
                        current_response = partial_response.chat_message
                        # Combine the label and response in the live display
                        display_text = Text.assemble(("Agent: ", "bold green"), (current_response, "green"))
                        live.update(display_text)


if __name__ == "__main__":

    load_dotenv()

    import asyncio
    asyncio.run(main())
