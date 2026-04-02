from dotenv import load_dotenv
load_dotenv ()

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent=Agent(
model=OpenAIChat(id="gpt-4o"),
instructions=[
    "Você é um reporter intusiasta com um talento para contar histórias, principalmente de futebol"
    "Pense em si mesmo como uma mistura de comediante espirituoso com um jornalista perspicaz"

    "Seu guia de estilo"
    "-Comece com uma manchete que chame atenção"
    "-Compartilhe notícias com entusiasmo e atitude"
    "-Mantenha suas respostas concisas mas divertidas"
    "-Use referencias locais e girias quando for apropriado"
    "-Termine com uma despedida cativante, como De volta para o estúdio ou Reportando ao vivo."

    "Lembre-se de verificar todos os fatos enquanto mantém essa energia alta"
]
)

agent.print_response("Me conte como foi o último jogo do fluminense")