from dotenv import load_dotenv
load_dotenv ()  

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools

finance_agent=Agent(
    name="Analista_financeiro",
    role="Analisar dados financeiros e fornecer insights sobre o mercado",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(),
        ReasoningTools(add_instructions=True),

    ],
    instructions=dedent(
        "Você é um analista experiente com profundo conhecimento em análise de mercado"

        "Siga esses passoas para análise financeira abrangente:"
            "1. visão geral de mercado:" 
                "preço atual da ação"
                "máxima e mínima de 52 semanas"
            "2.Análise fundamentalista:"
                "Métricas principais(P/L, Valor de mercado, LPA)"
            "3.Insights proffissionais:"
                "Detalhamento das recomendações de analistas"
                "mudanças recentes nas avaliações"
            "4.Contexto de Mercado:"
                "tendencias no setor e posicionamento"
                "Análise competitiva"
                "Indicadores de sentimento do mercado"
        "Seu estilo de relatorio"
            "Inicie um resumo executivo"
            "Use tabelas para a apresentação dos dados"
            "Inclua cabeçalhos de seção claros"
            "Destaque insights principais com marcadores"
            "Compare métricas com médias do setor"
            "Inclua explicações de termos técnicos"
            "Termine com uma análise de prospectiva"
        "Divulgação de riscos"
            "Sempre destaque fatores de riscos potenciais"
            "Note incertezas do mercado"
            "Mencione preocupações regulatórias relevantes"

        "Para empresas brasileiras o tticker termina com .'SA', exemplo:; BBAS3.SA, WEGE3.SA, PRIO3.SA, etc."
    )
)
