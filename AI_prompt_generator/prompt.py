PROMPT_CATEGORIES = {
    "Zero-Shot": """
Create a high-quality zero-shot prompt.

The prompt should clearly describe the task without providing examples.
Include:
- AI role
- Objective
- Context
- Requirements
- Constraints
- Expected output format
""",

    "Few-Shot": """
Create a high-quality few-shot prompt.

The prompt should teach the model the desired behavior using examples.
Include:
- AI role
- Objective
- Context
- 2-3 useful examples
- Requirements
- Expected output format
""",

    "Chain-of-Thought": """
Create a reasoning-focused prompt.

Ask the AI to carefully reason through the problem before producing
the final answer. Do not request hidden/private chain-of-thought.
Instead, request a concise explanation of the key reasoning or steps
needed to support the answer.

Include:
- Role
- Objective
- Context
- Important considerations
- Expected answer format
""",

    "Role-Based": """
Create a role-based prompt.

Give the AI a specific expert role appropriate to the user's task.

Include:
- Expert role
- Expertise
- Objective
- Context
- Responsibilities
- Constraints
- Output format
""",

    "Instruction-Based": """
Create a detailed instruction-based prompt.

Break the task into clear instructions and requirements.

Include:
- Role
- Goal
- Step-by-step instructions
- Constraints
- Quality requirements
- Output format
""",

    "Structured Output": """
Create a prompt that forces the AI to produce a clearly structured
response.

Specify the exact output structure, fields, sections, or JSON format
when appropriate.

Include:
- Role
- Objective
- Input requirements
- Output schema
- Validation requirements
""",

    "Creative": """
Create a creative-writing prompt.

Define the creative role, goal, audience, tone, style, constraints,
and desired output.
""",

    "Coding": """
Create a professional software-development prompt.

Include:
- Developer role
- Programming language/framework
- Project objective
- Functional requirements
- Technical requirements
- Error handling
- Security considerations
- Expected output
""",

    "Summarization": """
Create a professional summarization prompt.

Specify:
- What should be summarized
- Target audience
- Desired length
- Important information to preserve
- Information to exclude
- Output format
""",

    "Classification": """
Create a classification prompt.

Define:
- Classification task
- Available categories
- Classification rules
- Edge cases
- Required output format
"""
}


def build_generator_prompt(category, task, context, requirements):
    category_instructions = PROMPT_CATEGORIES[category]

    return f"""
You are an expert prompt engineer.

Your job is to transform the user's idea into a powerful,
clear, reusable AI prompt.

PROMPT CATEGORY:
{category}

CATEGORY GUIDELINES:
{category_instructions}

USER'S TASK:
{task}

ADDITIONAL CONTEXT:
{context}

ADDITIONAL REQUIREMENTS:
{requirements}

Create the final prompt.

Rules:
1. Make the prompt specific and unambiguous.
2. Add an appropriate AI role.
3. Clearly define the objective.
4. Include useful constraints.
5. Define the expected output.
6. Do not perform the user's task.
7. Do not explain how you created the prompt.
8. Return ONLY the final generated prompt.
"""