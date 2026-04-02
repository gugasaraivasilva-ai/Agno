from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent=Agent(
    id="Agente de scoulting",
    name="Olheiro de atletas",
    role="Responda perguntas sobre os atletas de futebol",
    instructions=[
        "Busque nas principais fontes confiáveis sobre o tema.",
        "Selecione cerca de 5-10 jogadores com idades entre 18 e 23 anos",
        "Não invente jogadores. Priorize jogadores com valor de mercado abaixo dos 10 milhões de euros com um alto potencial de evolução.",
        "Use a DuckDuckGoTools para buscas na internet.",
    ],
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
)
agent.print_response("Quais são os melhores meio campistas jovens do futebol brasileiro em 2026?")
