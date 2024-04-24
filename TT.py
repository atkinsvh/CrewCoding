import os
from crewai import Agent, Task, Crew

OPENAI_API_BASE = 'https://api.openai.com/v1'
OPENAI_MODEL_NAME_TEXT = 'gpt-3.5-turbo'  # For text generation
OPENAI_MODEL_NAME_IMAGE = 'dall-e-2'  # For image generation
OPENAI_API_KEY = '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'


class Agent:
    def __init__(self, role, goal, backstory, capabilities):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.capabilities = capabilities  # Capabilities could include 'text_generation' and 'image_generation'

class Task:
    def __init__(self, description, expected_output, agent):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent

class Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks
    
    def kickoff(self):
        results = {}
        for task in self.tasks:
            if 'text_generation' in task.agent.capabilities:
                # Simulate text generation
                results[task.description] = f"Generated Text for: {task.description}"
            if 'image_generation' in task.agent.capabilities:
                # Simulate image generation
                results[task.description] = f"Generated Image for: {task.description}"
        return results

# Define Agents
researcher = Agent(
    role='Project Management Tool Analyst',
    goal='Identify and evaluate futuristic project management tools',
    backstory="""Experienced in analyzing and implementing project management solutions 
                across various industries. Passionate about enhancing team productivity 
                and project outcomes through effective tool utilization.""",
    capabilities=['text_generation', 'image_generation']
)

writer = Agent(
    role='Content Creator for Project Management',
    goal='Create engaging and informative content on the latest project management tools',
    backstory="""Skilled in translating technical features into compelling stories. 
                Aims to empower project managers and teams with knowledge about cutting-edge tools.""",
    capabilities=['text_generation']
)

# Define Tasks
task1 = Task(
    description="Visualize the UI/UX of project management tools in 2024.",
    expected_output="High-definition images showcasing futuristic interface designs",
    agent=researcher
)

task2 = Task(
    description="""Analyze features, usability, and integration capabilities of 2024's 
                   project management tools.""",
    expected_output="Detailed report on futuristic project management tools",
    agent=researcher
)

task3 = Task(
    description="Draft an informative blog post about the latest project management tools.",
    expected_output="Engaging blog post for project managers",
    agent=writer
)

# Instantiate and run the crew with the tasks
crew = Crew(agents=[researcher, writer], tasks=[task1, task2, task3])

# Execute the tasks
results = crew.kickoff()

for task_description, result in results.items():
    print(f"{task_description}: {result}")

