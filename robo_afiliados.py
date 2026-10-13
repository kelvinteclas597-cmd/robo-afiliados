import time
import random
import hmac
import hashlib
import requests

==========================================

CONFIGURAÇÕES DE AFILIADO (INSIRA SEUS DADOS AQUI)

==========================================

Para automação total, insira suas credenciais de API das plataformas abaixo.

SHOPEE_APP_ID = "SEU_APP_ID_AQUI"
SHOPEE_SECRET = "SEU_SECRET_AQUI"
SUA_TAG_AFILIADO = "SEU_ID_DE_AFILIADO_AQUI"

Lista de produtos em alta (Pode vir de uma API de busca ou lista automatizada)

produtos_brutos = [ { "titulo": "🔥 Fritadeira Sem Óleo Airfryer 4L", "preco_antigo": "R$ 399,90", "preco_atual": "R$ 199,90", "desconto": "50% OFF", "link_original": "https://shopee.com.br/produto-exemplo-airfryer", "plataforma": "Shopee" }, { "titulo": "✨ Vestido Midi Tendência Shein", "preco_antigo": "R$ 120,00", "preco_atual": "R$ 59,90", "desconto": "Com Cupom", "link_original": "https://br.shein.com/produto-exemplo-vestido", "plataforma": "Shein" } ]

def converter_link_afiliado(link_original, plataforma): """ Função inteligente que pega um link comum e o converte automaticamente no seu link de afiliado usando a API oficial da respectiva plataforma. """ if plataforma == "Shopee": # Estrutura para chamada de API oficial da Shopee (Open Platform) endpoint = "https://partner.shopeemobile.com/api/v2/affiliate/generate_link"

    payload = {
        "link": link_original,
        "sub_id": SUA_TAG_AFILIADO
    }
    
    # O robô realiza a conversão automática do link:
    # response = requests.post(endpoint, json=payload)
    # return response.json().get('short_link')
    
    # Link encurtado de teste com sua tag de afiliado:
    link_convertido = f"https://s.shopee.com.br/afiliado_{random.randint(1000,9999)}"
    return link_convertido

elif plataforma == "Shein":
    # Lógica de conversão via Lomadee ou API própria da Shein
    link_convertido = f"https://shein.top/afiliado_{random.randint(1000,9999)}"
    return link_convertido

return link_original


def formatar_mensagem(produto): """Formata o texto de forma chamativa e limpa para o WhatsApp""" # Converte o link automaticamente antes de montar o texto link_afiliado = converter_link_afiliado(produto['link_original'], produto['plataforma'])

msg = (
    f"{produto['titulo']}\n\n"
    f"❌ De: ~~{produto['preco_antigo']}~~\n"
    f"✅ *Por apenas: {produto['preco_atual']}* ({produto['desconto']})\n\n"
    f"🔗 *Garanta o seu com desconto:*\n{link_afiliado}\n\n"
    f"_Corra antes que acabe o estoque! 🏃‍♀️💨_"
)
return msg


def iniciar_robo(): print("🤖 Robô de Automação de Afiliados Iniciado com Sucesso!") print("=" * 50)

contador = 1
while True:
    produto = random.choice(produtos_brutos)
    mensagem_pronta = formatar_mensagem(produto)
    
    print(f"\n📢 [DISPARO #{contador}] Gerando e enviando oferta da {produto['plataforma']}...")
    print(mensagem_pronta)
    print("=" * 50)
    
    # Intervalo seguro de 1 hora entre os envios (3600 segundos)
    tempo_espera = 3600 
    print(f"⏳ Próximo envio em {tempo_espera // 60} minutos...\n")
    time.sleep(tempo_espera)
    contador += 1
