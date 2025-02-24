# Orchestration Agent Example

This example demonstrates how to create an Orchestrator Agent that intelligently decides between using a search tool or a calculator tool based on user input.

## Features
- Intelligent tool selection between search and calculator tools
- Dynamic input/output schema handling
- Real-time date context provider
- Rich console output formatting
- Final answer generation based on tool outputs

## Getting Started

1. Clone the Atomic Agents repository:
   ```bash
   git clone https://github.com/BrainBlend-AI/atomic-agents
   ```

2. Navigate to the orchestration-agent directory:
   ```bash
   cd atomic-agents/atomic-examples/orchestration-agent
   ```

3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

4. Set up environment variables:
   Create a `.env` file in the `orchestration-agent` directory with:

   BASE_URL=http://localhost:11434/v1
   OPENAI_API_KEY=ollama

   SEARXNG_BASE_URL=https://searxng.domain.com
   SEARXNG_MAX_RESULTS=15

   FAST_LLM=llama3.1:8b
   SMART_LLM=qwen2.5:32b
   VISION_LLM=llama3.2-vision:11b

   Replace `localhost` if you are running ollama on a different machine.
   Replace 'https://searxng.domain.com' with your SearXNG domain name.


5. Install SearxNG (See: https://github.com/searxng/searxng)

6. Run the example:
   ```bash
   poetry run python orchestration_agent/orchestrator.py
   ```

## Components

### Input/Output Schemas

- **OrchestratorInputSchema**: Handles user input messages
- **OrchestratorOutputSchema**: Specifies tool selection and parameters
- **FinalAnswerSchema**: Formats the final response

### Tools
These tools were installed using the Atomic Assembler CLI (See the main README [here](../../README.md) for more info)
The agent orchestrates between two tools:
- **SearxNG Search Tool**: For queries requiring factual information
- **Calculator Tool**: For mathematical calculations

### Context Providers

- **CurrentDateProvider**: Provides the current date in YYYY-MM-DD format
