from dotenv import load_dotenv
load_dotenv ()

import asyncio

from agno.models.openai import OpenAIChat
from agno.team.team import Team

from teste05 import finance_agent
from teste04 import pesquisador_financeiro

agents_team=Team(
    name="Equipe de Análise Financeira",
    mode="collaborate",
    model=OpenAIChat(id="gpt-4o"),
    members=[
        finance_agent, 
        pesquisador_financeiro,
    ],
    instructions=[
        "Você é o coordenador de uma equipe de análise financeira.",
        "Você deve parar da discução quando a equipe chegar a um concenso sobre a análise",
        "Certifique-se de que tanto a pesquisaquanto a análise técnica sejam abordados",
        "O relatório final deve ser bem abrangente e estruturado",
    ],
    markdown=True,
    show_members_responses=True, 
)



if  __name__  =="__main__":
    asyncio.run(
        agents_team.aprint_response(
            input="iniciem a análise sobre o tema: 'Análise completa das ações do Banco do Brasil (BBAS3.SA) '",
            stream=True,
        )
    )