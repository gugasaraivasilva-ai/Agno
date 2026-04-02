from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.valyu import ValyuTools

load_dotenv ()

agent = Agent(
    id ="Agente de pesquisa",
    name = "Pesquisador DDG",
    role = "Responda perguntas baseados em contextos buscados na internet e em artigos científicos", 
    instructions = [
        "Busque as principais fontes confiáveis sobre o tema.",
        "Entregue uma saída concisa com: 5-10 fatos em bullets e um quadro de fontes com título + URL.",
        "Não invente links. Priorize sites oficiais, artigos e referências robustas.",
        "Use a ValyuTools para busca em artigos e o DuckDuckGoTools para buscas na internet.",
    ],
    model = OpenAIChat(id="gpt-4o"),
    tools = [DuckDuckGoTools(), ValyuTools()],
)

agent.print_response("Quais os principais artigos científicos sobre nutrição")