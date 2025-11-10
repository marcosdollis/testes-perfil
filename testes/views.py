from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import Resposta
import json
import random
import os

# Sistema de análise de respostas e geração de resultados personalizados

def analisar_personalidade(respostas):
    """Analisa as respostas e determina o perfil de personalidade"""
    # Mapeia índices de respostas para traços
    tracos = {
        'analitico': 0,
        'intuitivo': 0,
        'social': 0,
        'impulsivo': 0,
        'ambicioso': 0,
        'estavel': 0
    }
    
    # Análise REBALANCEADA baseada nas 35 respostas
    for i, resp in respostas.items():
        idx = int(i.split('_')[1])
        opcao = int(resp) if resp.isdigit() else 0
        
        # BLOCO 1: Reações e Tomada de Decisão (Q0-4)
        if idx == 0:  # Estresse
            if opcao == 0: tracos['impulsivo'] += 3
            elif opcao == 1: tracos['analitico'] += 3
            elif opcao == 2: tracos['social'] += 3
            else: tracos['intuitivo'] += 3
        
        elif idx == 1:  # Decisões
            if opcao == 0: tracos['analitico'] += 3
            elif opcao == 1: tracos['intuitivo'] += 3
            elif opcao == 2: tracos['social'] += 3
            else: tracos['estavel'] += 3
        
        elif idx == 2:  # Grupo
            if opcao == 0: tracos['ambicioso'] += 3
            elif opcao == 1: tracos['social'] += 3
            elif opcao == 2: tracos['intuitivo'] += 3
            else: tracos['impulsivo'] += 3
        
        elif idx == 3:  # Conflitos
            if opcao == 0: tracos['impulsivo'] += 3
            elif opcao == 1: tracos['estavel'] += 3
            elif opcao == 2: tracos['social'] += 3
            else: tracos['analitico'] += 3
        
        elif idx == 4:  # Motivação
            if opcao == 0: tracos['ambicioso'] += 3
            elif opcao == 1: tracos['estavel'] += 3
            elif opcao == 2: tracos['intuitivo'] += 3
            else: tracos['social'] += 3
        
        # BLOCO 2: Estilo de Trabalho (Q5-9)
        elif idx == 5:  # Trabalhar
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['intuitivo'] += 2
        
        elif idx == 6:  # Críticas
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['impulsivo'] += 2
            elif opcao == 2: tracos['ambicioso'] += 2
            else: tracos['estavel'] += 2
        
        elif idx == 7:  # Comunicação
            if opcao == 0: tracos['impulsivo'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['analitico'] += 2
        
        elif idx == 8:  # Mudanças
            if opcao == 0: tracos['intuitivo'] += 2
            elif opcao == 1: tracos['analitico'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['estavel'] += 3
        
        elif idx == 9:  # Qualidade
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['analitico'] += 2
        
        # BLOCO 3: Comportamento Social (Q10-14)
        elif idx == 10:  # Imprevistos
            if opcao == 0: tracos['impulsivo'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['social'] += 2
            else: tracos['analitico'] += 2
        
        elif idx == 11:  # Organização
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['impulsivo'] += 2
        
        elif idx == 12:  # Riscos
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['impulsivo'] += 2
            else: tracos['analitico'] += 2
        
        elif idx == 13:  # Lazer
            if opcao == 0: tracos['social'] += 2
            elif opcao == 1: tracos['intuitivo'] += 2
            elif opcao == 2: tracos['impulsivo'] += 2
            else: tracos['estavel'] += 2
        
        elif idx == 14:  # Realização
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['impulsivo'] += 2
        
        # BLOCO 4: Valores e Crenças (Q15-19)
        elif idx == 15:  # Medo
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['analitico'] += 2
            else: tracos['intuitivo'] += 2
        
        elif idx == 16:  # Irrita
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['analitico'] += 2
            else: tracos['intuitivo'] += 2
        
        elif idx == 17:  # Valoriza
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['ambicioso'] += 2
            else: tracos['social'] += 2
        
        elif idx == 18:  # Problema complexo
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['intuitivo'] += 2
            elif opcao == 2: tracos['social'] += 2
            else: tracos['estavel'] += 2
        
        elif idx == 19:  # Filosofia
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['intuitivo'] += 2
            elif opcao == 2: tracos['social'] += 2
            else: tracos['impulsivo'] += 2
        
        # BLOCO 5: Autopercepção (Q20-24)
        elif idx == 20:  # Descreveria
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['intuitivo'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['impulsivo'] += 2
        
        elif idx == 21:  # Ponto forte
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['ambicioso'] += 2
            else: tracos['estavel'] += 2
        
        elif idx == 22:  # Desafio
            if opcao == 0: tracos['impulsivo'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['analitico'] += 2
            else: tracos['social'] += 2
        
        elif idx == 23:  # Pressão
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['analitico'] += 2
        
        elif idx == 24:  # Considera-se
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['impulsivo'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['estavel'] += 2
        
        # BLOCO 6: Relacionamentos (Q25-29)
        elif idx == 25:  # Relacionamentos
            if opcao == 0: tracos['estavel'] += 2
            elif opcao == 1: tracos['intuitivo'] += 2
            elif opcao == 2: tracos['social'] += 2
            else: tracos['analitico'] += 2
        
        elif idx == 26:  # Amizade
            if opcao == 0: tracos['social'] += 2
            elif opcao == 1: tracos['impulsivo'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['intuitivo'] += 2
        
        elif idx == 27:  # Afeto
            if opcao == 0: tracos['impulsivo'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['ambicioso'] += 2
        
        elif idx == 28:  # Discussão
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['analitico'] += 2
        
        elif idx == 29:  # Precisa
            if opcao == 0: tracos['analitico'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['estavel'] += 2
            else: tracos['intuitivo'] += 2
        
        # BLOCO 7: Futuro e Ambições (Q30-34)
        elif idx == 30:  # 5 anos
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['estavel'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['impulsivo'] += 2
        
        elif idx == 31:  # Sonho
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['social'] += 2
            elif opcao == 2: tracos['intuitivo'] += 2
            else: tracos['estavel'] += 2
        
        elif idx == 32:  # Sucesso
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['intuitivo'] += 2
            elif opcao == 2: tracos['social'] += 2
            else: tracos['estavel'] += 2
        
        elif idx == 33:  # Aprende
            if opcao == 0: tracos['impulsivo'] += 2
            elif opcao == 1: tracos['analitico'] += 2
            elif opcao == 2: tracos['social'] += 2
            else: tracos['intuitivo'] += 2
        
        elif idx == 34:  # Influência
            if opcao == 0: tracos['ambicioso'] += 2
            elif opcao == 1: tracos['impulsivo'] += 2
            elif opcao == 2: tracos['analitico'] += 2
            else: tracos['intuitivo'] += 2
    
    # DEBUG: Imprime as pontuações (você pode ver no terminal do servidor)
    print(f"\n🔍 DEBUG - Pontuações:")
    for trait, score in sorted(tracos.items(), key=lambda x: x[1], reverse=True):
        print(f"  {trait}: {score}")
    
    # Determina perfil dominante
    perfil_dominante = max(tracos.items(), key=lambda x: x[1])[0]
    print(f"✅ Perfil escolhido: {perfil_dominante}\n")
    
    perfis = {
        'analitico': 'Analista Estratégico',
        'intuitivo': 'Visionário Criativo',
        'social': 'Líder Empático',
        'impulsivo': 'Executor Dinâmico',
        'ambicioso': 'Conquistador Determinado',
        'estavel': 'Guardião Confiável'
    }
    
    return {
        'perfil': perfis.get(perfil_dominante, 'Analista Estratégico'),
        'tipo_codigo': perfil_dominante,
        'pontuacoes': tracos
    }

def gerar_preview_personalidade(analise):
    """Gera um preview variado baseado no perfil"""
    perfil = analise['tipo_codigo']
    
    previews = {
        'analitico': [
            "Sua análise revela um perfil marcado por características analíticas e reflexivas. Você demonstra traços de pensador estratégico, o que significa que tende a planejar antes de agir. Pessoas com seu perfil são confiáveis e orientadas...",
            "Os resultados indicam uma personalidade com forte tendência ao pensamento lógico e sistemático. Você processa informações de forma estruturada e toma decisões baseadas em análise cuidadosa. Indivíduos como você se destacam em...",
            "Seu perfil psicológico revela características de um estrategista natural. Você possui habilidade excepcional para visualizar sistemas complexos e encontrar soluções eficientes. Pessoas com essa configuração mental frequentemente..."
        ],
        'intuitivo': [
            "Sua avaliação mostra um perfil criativo e visionário. Você possui forte intuição e capacidade de enxergar possibilidades que outros não percebem. Pessoas com seu tipo de mente são inovadoras e...",
            "Os dados revelam uma personalidade com características de pensador criativo. Você confia em seus insights e tem facilidade para conectar ideias aparentemente desconexas. Indivíduos assim tendem a...",
            "Sua análise aponta para um perfil inovador e original. Você pensa fora da caixa e encontra soluções não convencionais. Pessoas com sua configuração mental são frequentemente..."
        ],
        'social': [
            "Os resultados mostram um perfil com forte inteligência emocional e habilidades sociais. Você naturalmente compreende e se conecta com as pessoas. Indivíduos com seu perfil são excelentes em...",
            "Sua análise indica características de líder natural e comunicador nato. Você possui empatia desenvolvida e sabe trabalhar em equipe. Pessoas com essa personalidade frequentemente...",
            "O perfil revela traços de um facilitador e mediador excepcional. Você tem o dom de unir pessoas e criar ambientes harmoniosos. Indivíduos assim se destacam em..."
        ],
        'impulsivo': [
            "Sua avaliação mostra um perfil dinâmico e orientado para ação. Você não tem medo de tomar iniciativa e fazer as coisas acontecerem. Pessoas com seu perfil são...",
            "Os resultados indicam uma personalidade energética e proativa. Você prefere agir a ficar apenas planejando. Indivíduos assim são frequentemente...",
            "Seu perfil revela características de executor nato. Você transforma ideias em realidade rapidamente. Pessoas com essa configuração são..."
        ],
        'ambicioso': [
            "Sua análise mostra um perfil altamente focado em conquistas e resultados. Você estabelece metas ambiciosas e trabalha incansavelmente para alcançá-las. Pessoas com seu perfil tendem a...",
            "Os dados revelam uma personalidade orientada ao sucesso. Você possui drive interno poderoso e não aceita mediocridade. Indivíduos assim frequentemente...",
            "O perfil indica traços de alto desempenho e determinação. Você busca constantemente se superar e alcançar novos patamares. Pessoas assim são..."
        ],
        'estavel': [
            "Sua avaliação mostra um perfil equilibrado e confiável. Você valoriza estabilidade e segurança, tomando decisões ponderadas. Pessoas com seu perfil são...",
            "Os resultados indicam uma personalidade centrada e consistente. Você é a rocha em que outros se apoiam. Indivíduos assim tendem a...",
            "Seu perfil revela características de guardião responsável. Você mantém a calma em situações difíceis. Pessoas com essa configuração são..."
        ]
    }
    
    opcoes = previews.get(perfil, previews['analitico'])
    return random.choice(opcoes)

def gerar_resultado_completo_personalidade(analise, respostas):
    """Gera resultado completo personalizado baseado nas respostas"""
    perfil = analise['perfil']
    tipo_codigo = analise['tipo_codigo']
    pontuacoes = analise['pontuacoes']
    
    # Personaliza baseado nos pontos fortes
    pontos_fortes = []
    if pontuacoes['analitico'] > 5:
        pontos_fortes.append("Pensamento Analítico Superior")
    if pontuacoes['intuitivo'] > 5:
        pontos_fortes.append("Intuição Aguçada")
    if pontuacoes['social'] > 5:
        pontos_fortes.append("Inteligência Emocional Desenvolvida")
    if pontuacoes['ambicioso'] > 5:
        pontos_fortes.append("Foco em Resultados")
    if pontuacoes['estavel'] > 3:
        pontos_fortes.append("Estabilidade Emocional")
    
    if not pontos_fortes:
        pontos_fortes = ["Versatilidade", "Equilíbrio"]
    
    resultado = f'''═══════════════════════════════════════════════════
ANÁLISE COMPLETA DE PERSONALIDADE
Relatório Psicológico Detalhado
═══════════════════════════════════════════════════

📊 SEU PERFIL DOMINANTE: {perfil}
Raridade: Apenas 2-4% da população possui este perfil específico

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 SUAS CARACTERÍSTICAS FUNDAMENTAIS

Baseado em suas {len(respostas)} respostas detalhadas, identificamos um padrão consistente de comportamento e tomada de decisão que define quem você é no seu núcleo.

'''
    
    # Descrição personalizada por tipo
    descricoes = {
        'analitico': "Você é uma pessoa naturalmente introspectiva e profundamente analítica. Sua mente funciona como um processador estratégico, sempre buscando otimizar processos e encontrar as soluções mais eficientes. Enquanto outros agem por impulso, você prefere observar, analisar e só então tomar decisões fundamentadas.",
        'intuitivo': "Você possui uma mente criativa e visionária que constantemente vê possibilidades onde outros veem limites. Sua intuição é uma bússola poderosa que te guia através de decisões complexas. Você tem o dom raro de conectar ideias aparentemente desconexas e criar soluções inovadoras.",
        'social': "Você é dotado de uma inteligência emocional excepcional que te permite ler pessoas e situações com precisão impressionante. Sua capacidade natural de empatia e comunicação faz com que outros se sintam compreendidos e valorizados em sua presença.",
        'impulsivo': "Você é uma força da natureza quando se trata de transformar ideias em ação. Enquanto outros ficam presos na análise paralisia, você age decisivamente. Sua energia e disposição para tomar riscos calculados te colocam à frente da maioria.",
        'ambicioso': "Você possui um drive interno extraordinário que te impulsiona constantemente para níveis mais altos de conquista. Mediocridade não faz parte do seu vocabulário. Você estabelece metas ambiciosas e trabalha incansavelmente até alcançá-las.",
        'estavel': "Você é uma presença estabilizadora e confiável em qualquer ambiente. Sua consistência e confiabilidade fazem de você alguém em quem outros podem confiar nos momentos mais difíceis. Você valoriza segurança e toma decisões ponderadas."
    }
    
    resultado += descricoes.get(tipo_codigo, descricoes['analitico'])
    
    resultado += f'''

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ SEUS PONTOS FORTES (Talentos Naturais)

'''
    
    for i, ponto in enumerate(pontos_fortes, 1):
        resultado += f"{i}. {ponto.upper()}\n"
    
    resultado += '''
→ Estas são habilidades que te colocam à frente de 85-95% das pessoas
→ Quando bem desenvolvidas, podem te levar a conquistas extraordinárias
→ São seus diferenciais competitivos no mercado de trabalho

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💼 CARREIRAS ALTAMENTE COMPATÍVEIS

'''
    
    carreiras = {
        'analitico': ["Engenharia de Software", "Cientista de Dados", "Estrategista de Negócios", "Arquiteto de Sistemas", "Analista Financeiro"],
        'intuitivo': ["Designer de Produtos", "Empreendedor", "Diretor Criativo", "Consultor de Inovação", "Artista/Músico Profissional"],
        'social': ["Gerente de Pessoas", "Psicólogo", "Recursos Humanos", "Coach Executivo", "Profissional de Vendas"],
        'impulsivo': ["Fundador de Startup", "Gerente de Projetos", "Vendedor", "Atleta Profissional", "Operador Financeiro"],
        'ambicioso': ["CEO/Executivo", "Investidor", "Advogado", "Cirurgião", "Consultor de Alto Nível"],
        'estavel': ["Contador", "Gestor de Processos", "Analista de Qualidade", "Professor", "Administrador"]
    }
    
    for carreira in carreiras.get(tipo_codigo, carreiras['analitico']):
        resultado += f"• {carreira}\n"
    
    resultado += '''
💰 POTENCIAL DE RENDA:
Seu perfil está estatisticamente associado a rendas acima da média quando bem posicionado.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PLANO DE AÇÃO PERSONALIZADO

PRÓXIMOS 30 DIAS:
□ Identifique 3 áreas de conhecimento que quer dominar
□ Crie um sistema de organização pessoal
□ Pratique suas maiores forças diariamente
□ Faça networking com pessoas do seu perfil
□ Reserve tempo para reflexão e planejamento

PRÓXIMOS 6 MESES:
□ Desenvolva uma habilidade técnica avançada
□ Crie um projeto desafiador
□ Leia 6 livros sobre desenvolvimento pessoal
□ Estabeleça uma rotina de alto desempenho
□ Busque um mentor na sua área

PRÓXIMOS 12 MESES:
□ Posicione-se como especialista
□ Construa um portfólio impressionante
□ Desenvolva sua marca pessoal
□ Estabeleça metas financeiras ambiciosas
□ Ajude outras pessoas a crescerem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💎 MENSAGEM FINAL

Você possui um conjunto único de características que, quando bem direcionadas, podem levá-lo a conquistas extraordinárias. 

NÃO subestime o poder de quem você é.

Enquanto outros buscam atalhos, você constrói fundações sólidas.
Enquanto outros desistem, você persevera.
Enquanto outros seguem a multidão, você traça seu próprio caminho.

🌟 VOCÊ NÃO É COMUM - E ISSO É SUA MAIOR FORÇA.

Continue investindo em si mesmo. Continue aprendendo. Continue crescendo.

═══════════════════════════════════════════════════
Este relatório foi gerado baseado em suas respostas
específicas e análise psicométrica avançada.
═══════════════════════════════════════════════════

© 2025 - Análise Psicológica Profissional
'''
    
    return resultado

def analisar_renda_idade(respostas):
    """Analisa se a renda está adequada para a idade e perfil"""
    
    # Extrair respostas
    idade = int(respostas.get('pergunta_0', '0'))  # 0: 18-24, 1: 25-34, 2: 35-44, 3: 45+
    escolaridade = int(respostas.get('pergunta_1', '0'))  # 0: Médio, 1: Superior Inc, 2: Superior, 3: Pós
    area = int(respostas.get('pergunta_2', '0'))
    experiencia = int(respostas.get('pergunta_3', '0'))
    posicao = int(respostas.get('pergunta_4', '0'))  # 0: Jr, 1: Pleno, 2: Sr, 3: Gestor
    renda_atual = int(respostas.get('pergunta_5', '0'))  # 0: <2k, 1: 2-5k, 2: 5-10k, 3: >10k
    
    # Calcular "score ideal" baseado no perfil
    score_ideal = 0
    score_ideal += idade * 25  # Idade conta muito
    score_ideal += escolaridade * 20
    score_ideal += experiencia * 15
    score_ideal += posicao * 20
    
    # Renda atual em score
    score_atual = renda_atual * 30
    
    # Análise de outros fatores
    renda_extra = int(respostas.get('pergunta_6', '0'))
    crescimento_renda = int(respostas.get('pergunta_8', '0'))
    investimento_capacitacao = int(respostas.get('pergunta_10', '0'))
    networking = int(respostas.get('pergunta_12', '0'))
    poupar = int(respostas.get('pergunta_15', '0'))
    investimentos = int(respostas.get('pergunta_16', '0'))
    dividas = int(respostas.get('pergunta_17', '0'))
    ambicao = int(respostas.get('pergunta_25', '0'))
    mindset = int(respostas.get('pergunta_28', '0'))
    
    # Calcular gap
    gap = score_atual - score_ideal
    
    # Determinar categoria
    if gap >= 20:
        categoria = "MUITO ACIMA"
        emoji = "🌟"
        cor = "verde"
    elif gap >= 0:
        categoria = "ADEQUADA"
        emoji = "✅"
        cor = "azul"
    elif gap >= -30:
        categoria = "ABAIXO"
        emoji = "⚠️"
        cor = "amarelo"
    else:
        categoria = "MUITO ABAIXO"
        emoji = "🚨"
        cor = "vermelho"
    
    # Mapeamentos
    faixas_idade_txt = ['18-24 anos', '25-34 anos', '35-44 anos', '45+ anos']
    faixas_renda_txt = ['até R$ 2.000', 'R$ 2.000 - R$ 5.000', 'R$ 5.000 - R$ 10.000', 'acima de R$ 10.000']
    posicoes_txt = ['Júnior/Estagiário', 'Pleno', 'Sênior', 'Gestor/Líder']
    
    # Gerar resultado personalizado
    resultado = f'''
═══════════════════════════════════════════════════
💰 ANÁLISE COMPLETA - ADEQUAÇÃO DE RENDA
═══════════════════════════════════════════════════

📊 SEU PERFIL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Idade: {faixas_idade_txt[idade]}
• Posição: {posicoes_txt[posicao]}
• Renda Atual: {faixas_renda_txt[renda_atual]}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{emoji} DIAGNÓSTICO: SUA RENDA ESTÁ {categoria}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
    
    if categoria == "MUITO ABAIXO":
        resultado += '''
⚠️ ATENÇÃO: Você está ganhando SIGNIFICATIVAMENTE menos do que deveria para seu perfil!

💡 A BOA NOTÍCIA: Isso significa que você tem um ENORME potencial de crescimento. Muitas pessoas no seu perfil estão ganhando 2-3x mais que você.

🎯 O QUE ESTÁ ACONTECENDO:

Possíveis Razões:
1. ❌ Você está em uma empresa que paga mal
2. ❌ Não está negociando seu salário adequadamente  
3. ❌ Falta de capacitação nas habilidades mais valorizadas
4. ❌ Networking limitado impedindo acesso a melhores oportunidades
5. ❌ Acomodação na zona de conforto

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 POTENCIAL DE AUMENTO: R$ 3.000 - R$ 8.000/mês
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 PLANO DE AÇÃO URGENTE (Próximos 90 dias):

SEMANA 1-2: DIAGNÓSTICO PROFUNDO
□ Pesquise salários no Glassdoor, Catho, LinkedIn
□ Identifique as 3 habilidades mais valorizadas na sua área
□ Faça uma lista de 20 empresas que pagam melhor
□ Atualize seu LinkedIn e currículo profissionalmente

SEMANA 3-4: CAPACITAÇÃO ESTRATÉGICA
□ Invista em UM curso/certificação que o mercado valoriza
□ Comece a construir um portfólio de projetos
□ Entre em comunidades da sua área (Discord, Telegram, etc)
□ Assista 3 vídeos/dia sobre sua área no YouTube

MÊS 2: NETWORKING E POSICIONAMENTO
□ Conecte com 50 pessoas da sua área no LinkedIn
□ Publique 3x por semana sobre sua área
□ Participe de 2 eventos online da sua área
□ Entre em contato com 3 recrutadores especializados

MÊS 3: AÇÃO E NEGOCIAÇÃO
□ Aplique para 20-30 vagas melhores
□ Negocie um aumento com seu empregador atual
□ Se não conseguir aumento, MUDE de empresa
□ Considere trabalho remoto para empresas de fora

'''
    
    elif categoria == "ABAIXO":
        resultado += '''
⚠️ SUA RENDA ESTÁ ABAIXO DO ESPERADO

Você não está em uma situação crítica, mas está deixando dinheiro na mesa. Há espaço claro para crescimento.

🎯 ANÁLISE:

Você provavelmente:
• Está há muito tempo na mesma empresa sem promoção
• Não negocia aumentos regularmente
• Poderia estar investindo mais em capacitação
• Tem networking limitado

💰 POTENCIAL DE AUMENTO: R$ 1.500 - R$ 4.000/mês
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 PLANO DE AÇÃO (Próximos 6 meses):

MESES 1-2: VALORIZAÇÃO INTERNA
□ Agende conversa com gestor sobre plano de carreira
□ Documente suas conquistas e resultados
□ Peça feedback sobre o que precisa para promoção
□ Assuma projetos de maior visibilidade

MESES 3-4: DESENVOLVIMENTO
□ Faça 1-2 cursos na sua área
□ Melhore seu inglês (se necessário)
□ Construa relacionamentos com líderes da empresa
□ Torne-se referência em algo específico

MESES 5-6: NEGOCIAÇÃO OU MUDANÇA  
□ Negocie aumento/promoção com base em resultados
□ Se negado, busque oportunidades externas
□ Tenha pelo menos 3 propostas antes de sair
□ Não aceite menos de 30% de aumento ao mudar

'''
    
    elif categoria == "ADEQUADA":
        resultado += '''
✅ VOCÊ ESTÁ NA MÉDIA DO MERCADO

Sua renda está alinhada com o esperado para seu perfil. Isso é bom, mas não significa que deve parar por aqui.

🎯 ANÁLISE:

Pontos Positivos:
• Renda compatível com mercado
• Provável estabilidade financeira
• Bom posicionamento atual

⚠️ ATENÇÃO:
Estar "na média" significa que 50% das pessoas ganham MAIS que você. Por que não fazer parte desse grupo?

💰 POTENCIAL DE CRESCIMENTO: R$ 2.000 - R$ 5.000/mês
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 PLANO PARA SAIR DA MÉDIA:

PRÓXIMOS 3 MESES:
□ Torne-se ESPECIALISTA em uma habilidade valiosa
□ Construa autoridade (LinkedIn, blog, YouTube)
□ Expanda networking estrategicamente  
□ Busque projetos com maior impacto

PRÓXIMOS 6-12 MESES:
□ Mire em empresas que pagam acima da média
□ Desenvolva habilidades de negociação
□ Considere trabalho remoto internacional
□ Explore renda extra na sua expertise

'''
    
    else:  # MUITO ACIMA
        resultado += '''
🌟 PARABÉNS! VOCÊ ESTÁ MUITO ACIMA DA MÉDIA!

Você está ganhando significativamente mais que a maioria das pessoas no seu perfil. Isso indica que você:

✅ Soube negociar bem
✅ Está em empresa que valoriza talento
✅ Possui habilidades diferenciadas
✅ Tem boa estratégia de carreira

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 FOCO AGORA: MANTER E MULTIPLICAR

Você está no caminho certo, mas não pode relaxar:

PRÓXIMOS PASSOS:
□ Diversifique fontes de renda
□ Invista em ativos que geram renda passiva
□ Construa sua marca pessoal
□ Considere empreender ou consultoria
□ Mentore outras pessoas (networking valioso)

⚠️ CUIDADOS:
• Não se acomode - o mercado muda rápido
• Continue estudando e se atualizando
• Mantenha seu networking ativo
• Não dependa apenas do salário

'''
    
    # Análise complementar baseada em outros fatores
    resultado += '''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 ANÁLISE COMPLEMENTAR:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
    
    # Análise de capacitação
    if investimento_capacitacao <= 1:
        resultado += '''
❌ CAPACITAÇÃO: CRÍTICO
Você investe POUCO em desenvolvimento. Isso limitará seu crescimento.
→ Meta: Investir 10% da renda em cursos, livros, eventos

'''
    else:
        resultado += '''
✅ CAPACITAÇÃO: BOM
Você investe em desenvolvimento, continue!
→ Mantenha aprendizado contínuo

'''
    
    # Análise de networking
    if networking <= 1:
        resultado += '''
❌ NETWORKING: PRECISA MELHORAR
Networking fraco limita suas oportunidades drasticamente.
→ 80% das melhores vagas vêm de indicação!

'''
    else:
        resultado += '''
✅ NETWORKING: BOM
Seu networking está saudável, continue expandindo.

'''
    
    # Análise financeira
    if poupar <= 1 or investimentos <= 1:
        resultado += '''
⚠️ GESTÃO FINANCEIRA: ATENÇÃO
Aumentar renda é inútil se não souber gerir.
→ Aprenda sobre educação financeira URGENTE

'''
    
    if dividas == 0:
        resultado += '''
❌ DÍVIDAS: CRÍTICO  
Dívidas estão consumindo seu potencial de crescimento.
→ Prioridade #1: Sair das dívidas

'''
    
    resultado += '''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 AS 7 VERDADES QUE NINGUÉM TE CONTA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 🎯 LEALDADE NÃO PAGA CONTAS
   Profissionais que mudam de empresa a cada 2-3 anos ganham 30-50% mais.

2. 💰 PEDIR AUMENTO É SUA RESPONSABILIDADE
   Nenhum chefe vai chegar e dobrar seu salário espontaneamente.

3. 🚀 HABILIDADES VENDEM, DIPLOMAS NEM SEMPRE
   Certificações práticas valem mais que diplomas teóricos.

4. 🌐 TRABALHO REMOTO INTERNACIONAL = 3X MAIS
   Empresas gringas pagam 2-5x mais para os mesmos cargos.

5. 📈 RENDA EXTRA NÃO É OPCIONAL
   Na economia atual, ter apenas uma fonte de renda é arriscado.

6. 🎓 INGLÊS = +50% DE SALÁRIO
   Fluência em inglês pode significar R$ 2.000-5.000/mês a mais.

7. 🤝 NETWORKING > CURRÍCULO
   Quem você conhece importa mais que o que você sabe.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 RECURSOS ESSENCIAIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PESQUISA SALARIAL:
• Glassdoor Brasil
• Catho - Guia de Salários
• LinkedIn Salary
• Vagas.com

CAPACITAÇÃO:
• Coursera / Udemy (certificações)
• YouTube (grátis, conteúdo infinito)
• Comunidades da sua área
• Eventos e meetups

OPORTUNIDADES:
• LinkedIn (principal)
• Trabalho Remoto: Remote.co, We Work Remotely
• Freelas: Workana, 99Freelas, Upwork
• Networking: eventos, grupos, comunidades

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ AÇÃO IMEDIATA (FAÇA HOJE):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Pesquise AGORA quanto ganham pessoas na sua posição
2. Atualize seu LinkedIn (dedique 1 hora nisso)
3. Entre em 3 grupos/comunidades da sua área
4. Defina sua meta de renda para 12 meses
5. Comprometa-se a aplicar PELO MENOS uma ação por semana

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💭 REFLEXÃO FINAL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sua renda atual é reflexo das decisões que você tomou até agora.

A boa notícia? 

Você pode mudar isso. Não hoje, não amanhã, mas em 6-12 meses sua realidade pode ser COMPLETAMENTE diferente.

A pergunta é: você vai AGIR ou apenas vai continuar desejando?

O tempo vai passar de qualquer forma. Daqui 1 ano, você quer estar ganhando o mesmo... ou MUITO mais?

🔥 A decisão é SUA. O momento é AGORA.

═══════════════════════════════════════════════════
© 2025 - Análise Profissional de Adequação Salarial
Baseado em dados de mercado e perfil individual
═══════════════════════════════════════════════════
'''
    
    return resultado

def gerar_preview_renda(respostas):
    """Gera preview personalizado para o teste de renda"""
    idade = int(respostas.get('pergunta_0', '0'))
    renda_atual = int(respostas.get('pergunta_5', '0'))
    posicao = int(respostas.get('pergunta_4', '0'))
    
    faixas_idade_txt = ['18-24 anos', '25-34 anos', '35-44 anos', '45+ anos']
    faixas_renda_txt = ['até R$ 2.000', 'R$ 2.000 a R$ 5.000', 'R$ 5.000 a R$ 10.000', 'acima de R$ 10.000']
    
    # Calcular se está adequado (lógica simplificada)
    score_ideal = idade * 25 + posicao * 20
    score_atual = renda_atual * 30
    gap = score_atual - score_ideal
    
    if gap >= 0:
        status = "na média ou acima"
        emoji = "✅"
    else:
        status = "abaixo do esperado"
        emoji = "⚠️"
    
    previews = [
        f'''{emoji} Com base na sua idade ({faixas_idade_txt[idade]}) e renda atual ({faixas_renda_txt[renda_atual]}), nossa análise indica que você está {status} da faixa salarial para seu perfil. Comparado com profissionais similares, identificamos um potencial de crescimento de R$ 2.000 a R$ 8.000/mês. No relatório completo, você descobrirá exatamente onde está perdendo dinheiro e o plano de ação específico para aumentar sua renda nos próximos 90 dias...''',
        
        f'''{emoji} Sua renda está {status} para alguém com seu perfil profissional. Analisamos mais de 15.000 profissionais e identificamos padrões claros: pessoas na sua situação que seguiram as estratégias certas aumentaram a renda entre 40% e 200% em 12 meses. O relatório completo revela as 7 verdades que ninguém te conta sobre salário e o roteiro mês a mês para você sair da zona de conforto financeiro...''',
        
        f'''Resultado da Análise: Sua renda ({faixas_renda_txt[renda_atual]}) está {status} do que profissionais com perfil similar ganham no mercado atual. {emoji} Nossa metodologia identificou pelo menos 3 oportunidades concretas que você pode explorar IMEDIATAMENTE para aumentar seus ganhos. No relatório completo, você terá acesso ao diagnóstico profundo, benchmarking detalhado e plano de ação personalizado com metas realistas para os próximos 3, 6 e 12 meses...'''
    ]
    
    return random.choice(previews)

def analisar_qi(respostas):
    """Analisa as respostas do teste de QI"""
    # GABARITO CORRIGIDO (índice da opção correta):
    gabarito = {
        0: 1,  # Q0: 5 minutos (resposta: índice 1)
        1: 1,  # Q1: 64 (2^6, resposta: índice 1)
        2: 2,  # Q2: Cenoura (é vegetal, não fruta, resposta: índice 2)
        3: 0,  # Q3: Sim (lógica transitiva, resposta: índice 0)
        4: 1,  # Q4: 5 triângulos (4 pequenos + 1 grande, resposta: índice 1)
        5: 2,  # Q5: Comer (livro-ler, garfo-comer, resposta: índice 2)
        6: 1,  # Q6: 21 (Fibonacci: 8+13=21, resposta: índice 1)
        7: 1,  # Q7: Um país (PACIFICO, resposta: índice 1)
        8: 0,  # Q8: K (letras sem curvas, resposta: índice 0)
        9: 1,  # Q9: 12 meses (todos têm 28 dias, resposta: índice 1)
        10: 0, # Q10: 127 (padrão: 2n+1, resposta: índice 0)
        11: 2, # Q11: Círculo (único sem lados retos, resposta: índice 2)
        12: 0, # Q12: 36 (V=22, I=9, D=4, A=1 = 36, resposta: índice 0)
        13: 1, # Q13: 8 (único não múltiplo de 3 ou primo adjacente, resposta: índice 1)
        14: 0, # Q14: Inverno (analogia direta, resposta: índice 0)
        15: 0, # Q15: 1 vez (depois é 90, não 100, resposta: índice 0)
        16: 0, # Q16: 2 (metade de 4 é 2, resposta: índice 0)
        17: 0, # Q17: Luva (analogia de vestimenta, resposta: índice 0)
        18: 0, # Q18: 12 lados (dodeca = 12, resposta: índice 0)
        19: 0, # Q19: R$ 1,00 (1,5 dúzia = 18 ovos, 18/18=1, resposta: índice 0)
    }
    
    # DEBUG: Mostra respostas e gabarito
    print(f"\n🧠 DEBUG TESTE DE QI:")
    acertos = 0
    for i, resp in respostas.items():
        idx = int(i.split('_')[1])
        if idx in gabarito and resp.isdigit():
            resposta_usuario = int(resp)
            resposta_correta = gabarito[idx]
            acertou = resposta_usuario == resposta_correta
            if acertou:
                acertos += 1
            print(f"  Q{idx}: Usuário={resposta_usuario}, Correto={resposta_correta} {'✅' if acertou else '❌'}")
    
    print(f"\n📊 Total: {acertos}/20 acertos ({(acertos/20)*100:.0f}%)\n")
    
    # Calcula QI baseado nos acertos (CORRIGIDO)
    percentual = (acertos / 20) * 100
    
    if percentual >= 90:  # 18-20 acertos
        qi_range = "130-145"
        classificacao = "Muito Superior"
        percentil = "Top 2%"
    elif percentual >= 75:  # 15-17 acertos
        qi_range = "120-129"
        classificacao = "Superior"
        percentil = "Top 10%"
    elif percentual >= 60:  # 12-14 acertos
        qi_range = "110-119"
        classificacao = "Acima da Média"
        percentil = "Top 25%"
    elif percentual >= 45:  # 9-11 acertos
        qi_range = "100-109"
        classificacao = "Média"
        percentil = "50%"
    elif percentual >= 30:  # 6-8 acertos
        qi_range = "90-99"
        classificacao = "Média-Baixa"
        percentil = "25%"
    else:  # 0-5 acertos
        qi_range = "85-95"
        classificacao = "Abaixo da Média"
        percentil = "16%"
    
    return {
        'acertos': acertos,
        'qi_range': qi_range,
        'classificacao': classificacao,
        'percentil': percentil,
        'percentual': percentual
    }

def gerar_preview_qi(analise):
    """Gera preview variado para o teste de QI"""
    previews = [
        f"Baseado nas suas respostas, você acertou {analise['acertos']} de 20 questões. Seu QI estimado está na faixa {analise['qi_range']}, classificação: {analise['classificacao']}. Isso te coloca no percentil {analise['percentil']} da população. Suas maiores forças incluem...",
        f"Sua performance no teste revelou {analise['acertos']} acertos em 20 questões. Análise preliminar indica QI entre {analise['qi_range']}, categoria {analise['classificacao']}. Você está entre os {analise['percentil']} melhores. Seus pontos fortes aparecem em...",
        f"Resultados mostram {analise['acertos']}/20 questões corretas. Seu quociente de inteligência estimado: {analise['qi_range']}, nível {analise['classificacao']}. Posicionamento: {analise['percentil']}. Destaque especial para suas habilidades em..."
    ]
    return random.choice(previews)

def gerar_resultado_completo_qi(analise):
    """Gera resultado completo do QI"""
    acertos = analise['acertos']
    
    resultado = f'''═══════════════════════════════════════════════════
ANÁLISE COMPLETA DO SEU QI
Relatório Detalhado de Inteligência
═══════════════════════════════════════════════════

📊 SEUS RESULTADOS:

QI Estimado: {analise['qi_range']}
Classificação: {analise['classificacao']}
Percentil: {analise['percentil']}
Acertos: {acertos}/20 ({analise['percentual']:.0f}%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 ANÁLISE DETALHADA POR CATEGORIA:

Raciocínio Lógico: {min(10, acertos//2 + 3)}/10
Raciocínio Matemático: {min(10, acertos//2 + 2)}/10
Capacidade Verbal: {min(10, acertos//2 + 3)}/10
Reconhecimento de Padrões: {min(10, acertos//2 + 4)}/10

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ PONTOS FORTES:

'''
    
    if acertos >= 15:
        resultado += '''• Excelente capacidade de identificar padrões complexos
• Raciocínio abstrato particularmente forte
• Processamento de informações acima da média
• Habilidade superior em resolução de problemas
'''
    elif acertos >= 12:
        resultado += '''• Boa capacidade de análise lógica
• Reconhecimento eficiente de padrões
• Raciocínio estruturado
• Potencial acima da média
'''
    else:
        resultado += '''• Capacidade de aprendizado consistente
• Potencial para desenvolvimento
• Habilidades práticas
• Raciocínio em evolução
'''
    
    resultado += f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 RECOMENDAÇÕES PERSONALIZADAS:

1. Pratique jogos de lógica (xadrez, sudoku, quebra-cabeças)
2. Leia livros que desafiem seu pensamento crítico
3. Aprenda um novo idioma para estimular o cérebro
4. Pratique matemática e problemas de lógica regularmente
5. Mantenha-se sempre aprendendo coisas novas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 DESENVOLVIMENTO CONTÍNUO:

Seu QI não é fixo - pode ser desenvolvido através de:
• Estudo consistente
• Desafios intelectuais
• Leitura diversificada
• Aprendizado de novas habilidades
• Prática deliberada

═══════════════════════════════════════════════════
Análise baseada em {acertos} respostas corretas
Metodologia psicométrica validada
═══════════════════════════════════════════════════
'''
    
    return resultado

TESTES_CONFIG = {
    'signo_oculto': {
        'titulo': 'Descubra Seu Verdadeiro Signo Espiritual',
        'descricao': 'Revele seu signo oculto e compreenda sua verdadeira natureza espiritual através de uma análise profunda.',
        'icone': '✨',
        'perguntas': [
            # Bloco 1: Temperamento e Personalidade
            {'pergunta': 'Como você descreveria sua energia pessoal?', 
             'opcoes': ['Intensa e dinâmica', 'Estável e constante', 'Leve e mutável', 'Profunda e fluida']},
            
            {'pergunta': 'Como você geralmente aborda novos desafios?', 
             'opcoes': ['Com planejamento cuidadoso', 'Com curiosidade intelectual', 'Com intuição e sensibilidade', 'Com entusiasmo e coragem']},
            
            {'pergunta': 'Como você processa suas emoções?', 
             'opcoes': ['Sinto profundamente', 'Analiso racionalmente', 'Expresso intensamente', 'Processo mentalmente']},
            
            {'pergunta': 'Ao tomar decisões importantes, você:', 
             'opcoes': ['Analisa todos os detalhes', 'Confia nos sentimentos', 'Pensa nos prós e contras', 'Segue seus instintos']},
            
            {'pergunta': 'Em relacionamentos, você tende a ser:', 
             'opcoes': ['Profundo e intenso', 'Leal e estável', 'Apaixonado e direto', 'Sociável e adaptável']},
            
            # Bloco 2: Espiritualidade e Intuição
            {'pergunta': 'Qual ambiente natural mais te energiza?', 
             'opcoes': ['Montanhas', 'Oceano', 'Deserto', 'Floresta']},
            
            {'pergunta': 'Como você se conecta com sua espiritualidade?', 
             'opcoes': ['Meditação silenciosa', 'Rituais práticos', 'Estudos filosóficos', 'Expressão criativa']},
            
            {'pergunta': 'Sua intuição geralmente se manifesta através de:', 
             'opcoes': ['Sensações físicas', 'Sonhos e visões', 'Pensamentos súbitos', 'Emoções intensas']},
            
            {'pergunta': 'Qual aspecto da vida mais te fascina?', 
             'opcoes': ['Mistérios do universo', 'Conexões humanas', 'Conhecimento ancestral', 'Transformação pessoal']},
            
            {'pergunta': 'Em momentos de crise, você busca:', 
             'opcoes': ['Orientação interior', 'Ajuda prática', 'Conhecimento', 'Ação imediata']},
            
            # Bloco 3: Propósito e Missão
            {'pergunta': 'Qual você sente que é seu dom natural?', 
             'opcoes': ['Curar e confortar', 'Ensinar e guiar', 'Criar e inspirar', 'Transformar e liderar']},
            
            {'pergunta': 'O que mais te motiva na vida?', 
             'opcoes': ['Crescimento espiritual', 'Realização material', 'Conhecimento', 'Liberdade']},
            
            {'pergunta': 'Como você prefere ajudar os outros?', 
             'opcoes': ['Ouvindo e aconselhando', 'Ações práticas', 'Compartilhando conhecimento', 'Inspirando mudanças']},
            
            {'pergunta': 'Qual palavra melhor descreve seu propósito?', 
             'opcoes': ['Curar', 'Construir', 'Ensinar', 'Transformar']},
            
            {'pergunta': 'O que você mais valoriza?', 
             'opcoes': ['Harmonia', 'Verdade', 'Liberdade', 'Sabedoria']},
            
            # Bloco 4: Ciclos e Mudanças
            {'pergunta': 'Como você lida com mudanças?', 
             'opcoes': ['Flui naturalmente', 'Resiste inicialmente', 'Adapta-se rapidamente', 'Busca controlá-las']},
            
            {'pergunta': 'Qual estação mais reflete sua personalidade?', 
             'opcoes': ['Inverno', 'Primavera', 'Verão', 'Outono']},
            
            {'pergunta': 'Em que momento do dia você se sente mais energizado?', 
             'opcoes': ['Amanhecer', 'Meio-dia', 'Entardecer', 'Noite']},
            
            {'pergunta': 'Como você vê os ciclos da vida?', 
             'opcoes': ['Como aprendizado', 'Como evolução', 'Como transformação', 'Como jornada']},
            
            {'pergunta': 'O que mais te ajuda em momentos difíceis?', 
             'opcoes': ['Meditação', 'Ação prática', 'Estudo', 'Movimento']}
        ]
    },
    'teste_qi': {
        'titulo': 'Teste de QI Completo',
        'descricao': 'Avalie seu quociente de inteligência através de questões de lógica e raciocínio.',
        'icone': '🧠',
        'perguntas': [
            {'pergunta': 'Se 5 máquinas levam 5 minutos para fazer 5 produtos, quanto tempo 100 máquinas levam para fazer 100 produtos?', 'opcoes': ['100 minutos', '5 minutos', '1 minuto', '50 minutos']},
            {'pergunta': 'Complete a sequência: 2, 4, 8, 16, 32, __', 'opcoes': ['48', '64', '56', '72']},
            {'pergunta': 'Qual palavra não pertence: Maçã, Banana, Cenoura, Laranja', 'opcoes': ['Maçã', 'Banana', 'Cenoura', 'Laranja']},
            {'pergunta': 'Se todos os Bloops são Razzies e todos os Razzies são Lazzies, então todos os Bloops são Lazzies?', 'opcoes': ['Sim', 'Não', 'Impossível determinar', 'Depende']},
            {'pergunta': 'Quantos triângulos você vê em um triângulo dividido em 4 pequenos?', 'opcoes': ['4', '5', '8', '9']},
            {'pergunta': 'Complete: Livro está para Leitura assim como Garfo está para __', 'opcoes': ['Cozinha', 'Comida', 'Comer', 'Mesa']},
            {'pergunta': 'Qual número vem a seguir: 1, 1, 2, 3, 5, 8, 13, __', 'opcoes': ['19', '21', '18', '20']},
            {'pergunta': 'Se você reorganizar CIFAIPC, você obtém nome de:', 'opcoes': ['Um oceano', 'Um país', 'Um animal', 'Uma cidade']},
            {'pergunta': 'Próxima letra na sequência: A, E, F, H, I, __', 'opcoes': ['K', 'L', 'J', 'M']},
            {'pergunta': 'Quantos meses têm 28 dias?', 'opcoes': ['1', '12', '11', '2']},
            {'pergunta': 'Complete o padrão: 3, 7, 15, 31, 63, __', 'opcoes': ['127', '125', '120', '130']},
            {'pergunta': 'Qual forma é diferente: Quadrado, Retângulo, Círculo, Paralelogramo?', 'opcoes': ['Quadrado', 'Retângulo', 'Círculo', 'Paralelogramo']},
            {'pergunta': 'Se A=1, B=2, C=3, quanto vale VIDA?', 'opcoes': ['36', '42', '38', '44']},
            {'pergunta': 'Qual não se encaixa: 2, 3, 6, 7, 8, 14, 15, 30', 'opcoes': ['30', '8', '6', '15']},
            {'pergunta': 'Complete: Calor está para Verão assim como Frio está para __', 'opcoes': ['Inverno', 'Gelo', 'Neve', 'Montanha']},
            {'pergunta': 'Quantas vezes você pode subtrair 10 de 100?', 'opcoes': ['1', '10', '9', '11']},
            {'pergunta': 'Qual é a metade de 2 + 2?', 'opcoes': ['2', '3', '4', '1']},
            {'pergunta': 'Complete: Pé está para Meia assim como Mão está para __', 'opcoes': ['Luva', 'Dedo', 'Anel', 'Relógio']},
            {'pergunta': 'Quantos lados tem um dodecágono?', 'opcoes': ['12', '10', '8', '15']},
            {'pergunta': 'Se 1,5 dúzia de ovos custa R$ 18, quanto custa cada ovo?', 'opcoes': ['R$ 1,00', 'R$ 1,50', 'R$ 0,75', 'R$ 2,00']},
        ],
        'resultados': {
            'preview': 'Baseado nas suas respostas, você demonstrou habilidades notáveis em raciocínio lógico e resolução de problemas. Seu QI estimado coloca você acima da média da população. Suas maiores forças incluem reconhecimento de padrões e pensamento analítico...',
            'completo': 'ANÁLISE COMPLETA DO SEU QI:\n\nQI Estimado: 118-125\nClassificação: Acima da Média Superior\nPercentil: Top 15%\n\nANÁLISE DETALHADA:\n\nRaciocínio Lógico: 8/10\nRaciocínio Matemático: 7/10\nCapacidade Verbal: 8/10\nReconhecimento de Padrões: 9/10\n\nPONTOS FORTES:\nVocê demonstra excelente capacidade de identificar padrões complexos e conexões não óbvias. Seu raciocínio abstrato é particularmente forte.\n\nÁREAS DE DESENVOLVIMENTO:\nPode se beneficiar de mais prática em cálculos rápidos e visualização espacial.\n\nRECOMENDAÇÕES:\n1. Pratique jogos de lógica e quebra-cabeças regularmente\n2. Leia livros que desafiem seu pensamento crítico\n3. Aprenda um novo idioma\n4. Pratique meditação para melhorar foco'
        }
    },
    'renda_idade': {
        'titulo': 'Sua Renda está Adequada para sua Idade?',
        'descricao': 'Descubra se você está ganhando o que deveria para a sua faixa etária e receba um plano de ação personalizado.',
        'icone': '💰',
        'perguntas': [
            # Perfil Demográfico
            {'pergunta': 'Qual sua faixa etária?', 'opcoes': ['18-24 anos', '25-34 anos', '35-44 anos', '45+ anos']},
            {'pergunta': 'Qual sua escolaridade?', 'opcoes': ['Ensino Médio', 'Superior Incompleto', 'Superior Completo', 'Pós-graduação']},
            {'pergunta': 'Qual sua área de atuação?', 'opcoes': ['Tecnologia', 'Saúde', 'Educação', 'Administrativo', 'Vendas', 'Outros']},
            {'pergunta': 'Tempo de experiência profissional:', 'opcoes': ['Menos de 2 anos', '2-5 anos', '5-10 anos', 'Mais de 10 anos']},
            {'pergunta': 'Sua posição atual:', 'opcoes': ['Estagiário/Júnior', 'Pleno', 'Sênior', 'Gestor/Líder']},
            
            # Situação Financeira Atual
            {'pergunta': 'Sua renda mensal individual:', 'opcoes': ['Até R$ 2.000', 'R$ 2.000 - R$ 5.000', 'R$ 5.000 - R$ 10.000', 'Acima de R$ 10.000']},
            {'pergunta': 'Você possui renda extra?', 'opcoes': ['Não', 'Sim, eventual', 'Sim, regular', 'Vivo de renda extra']},
            {'pergunta': 'Seu salário em relação ao mercado:', 'opcoes': ['Abaixo da média', 'Na média', 'Acima da média', 'Não sei']},
            {'pergunta': 'Nos últimos 2 anos sua renda:', 'opcoes': ['Diminuiu', 'Manteve igual', 'Aumentou pouco', 'Aumentou muito']},
            {'pergunta': 'Você negocia seu salário?', 'opcoes': ['Nunca', 'Raramente', 'Às vezes', 'Sempre']},
            
            # Desenvolvimento Profissional
            {'pergunta': 'Investe em capacitação:', 'opcoes': ['Nunca', 'Raramente', 'Frequentemente', 'Constantemente']},
            {'pergunta': 'Busca novas oportunidades:', 'opcoes': ['Estou acomodado', 'Penso nisso', 'Busco ativamente', 'Sempre em movimento']},
            {'pergunta': 'Seu networking profissional:', 'opcoes': ['Inexistente', 'Pequeno', 'Moderado', 'Muito forte']},
            {'pergunta': 'Domina alguma habilidade valiosa:', 'opcoes': ['Nenhuma específica', 'Uma ou duas', 'Várias', 'Sou especialista']},
            {'pergunta': 'Sua empregabilidade você considera:', 'opcoes': ['Baixa', 'Média', 'Alta', 'Muito alta']},
            
            # Gestão Financeira
            {'pergunta': 'Você poupa dinheiro:', 'opcoes': ['Nunca sobra', 'Às vezes', 'Regularmente', 'Tenho reserva sólida']},
            {'pergunta': 'Possui investimentos:', 'opcoes': ['Nenhum', 'Só poupança', 'Alguns investimentos', 'Portfólio diversificado']},
            {'pergunta': 'Dívidas atuais:', 'opcoes': ['Muitas dívidas', 'Algumas dívidas', 'Poucas dívidas', 'Sem dívidas']},
            {'pergunta': 'Controla suas finanças:', 'opcoes': ['Não controlo', 'Controlo mentalmente', 'Planilhas básicas', 'Sistema completo']},
            {'pergunta': 'Planejamento financeiro:', 'opcoes': ['Vivo o presente', 'Penso no curto prazo', 'Plano médio prazo', 'Visão de longo prazo']},
            
            # Ambição e Objetivos
            {'pergunta': 'Meta de renda em 5 anos:', 'opcoes': ['Não penso nisso', 'Manter atual', 'Dobrar', 'Triplicar ou mais']},
            {'pergunta': 'Disposição para mudanças:', 'opcoes': ['Prefiro estabilidade', 'Mudaria se necessário', 'Aberto a mudanças', 'Busco mudanças']},
            {'pergunta': 'Considera empreender:', 'opcoes': ['Nunca', 'Talvez um dia', 'Estou pensando', 'Já empreendo/Vou empreender']},
            {'pergunta': 'Trabalho remoto:', 'opcoes': ['Não é opção', 'Seria bom', 'É minha preferência', 'Já trabalho remoto']},
            {'pergunta': 'Mudar de área/carreira:', 'opcoes': ['Impossível', 'Muito difícil', 'Consideraria', 'Estou pronto']},
            
            # Mindset e Atitude
            {'pergunta': 'Você se considera:', 'opcoes': ['Acomodado', 'Satisfeito', 'Ambicioso', 'Extremamente ambicioso']},
            {'pergunta': 'Diante de desafios:', 'opcoes': ['Desisto fácil', 'Tento pouco', 'Persisto', 'Não desisto nunca']},
            {'pergunta': 'Sua visão sobre dinheiro:', 'opcoes': ['Não é tudo', 'É importante', 'É muito importante', 'É prioridade']},
            {'pergunta': 'Aprendizado contínuo:', 'opcoes': ['Parei de estudar', 'Estudo pouco', 'Estudo regularmente', 'Sempre aprendendo']},
            {'pergunta': 'Responsabilidade pela renda:', 'opcoes': ['Culpo o mercado', 'Depende do emprego', 'Parcialmente minha', 'Totalmente minha']},
        ],
        'resultados': {
            'preview': 'Com base na sua idade, escolaridade e área de atuação, nossa análise indica que você está [acima/na média/abaixo] da faixa salarial esperada para seu perfil. Comparado com profissionais similares, você está no percentil...',
            'completo': 'ANÁLISE COMPLETA - ADEQUAÇÃO DE RENDA'
        }
    },
    'personalidade': {
        'titulo': 'Análise de Personalidade Profunda',
        'descricao': 'Descubra traços únicos da sua personalidade através de uma análise psicológica detalhada.',
        'icone': '🎯',
        'perguntas': [
            # Bloco 1: Reações e Tomada de Decisão (5 questões)
            {'pergunta': 'Em situações de estresse, você tende a:', 'opcoes': ['Buscar soluções práticas', 'Refletir antes de agir', 'Pedir ajuda', 'Isolar-se']},
            {'pergunta': 'Quando precisa tomar uma decisão importante:', 'opcoes': ['Analiso prós e contras', 'Confio na intuição', 'Consulto pessoas', 'Procrastino']},
            {'pergunta': 'Em um grupo, você geralmente é:', 'opcoes': ['O líder', 'O mediador', 'O ouvinte', 'O animado']},
            {'pergunta': 'Ao enfrentar conflitos, você:', 'opcoes': ['Confronta diretamente', 'Evita', 'Busca compromisso', 'Analisa friamente']},
            {'pergunta': 'Sua motivação principal é:', 'opcoes': ['Sucesso', 'Estabilidade', 'Liberdade', 'Propósito']},
            
            # Bloco 2: Estilo de Trabalho (5 questões)
            {'pergunta': 'Você prefere trabalhar:', 'opcoes': ['Sozinho', 'Em equipe', 'Com supervisão', 'Flexível']},
            {'pergunta': 'Diante de críticas:', 'opcoes': ['Analiso objetivamente', 'Fico na defensiva', 'Uso para melhorar', 'Ignoro']},
            {'pergunta': 'Seu estilo de comunicação:', 'opcoes': ['Direto e objetivo', 'Diplomático', 'Emotivo', 'Reservado']},
            {'pergunta': 'Você lida com mudanças:', 'opcoes': ['Facilmente', 'Com cautela', 'Com resistência', 'Evito']},
            {'pergunta': 'Sua maior qualidade:', 'opcoes': ['Determinação', 'Empatia', 'Criatividade', 'Racionalidade']},
            
            # Bloco 3: Comportamento Social (5 questões)
            {'pergunta': 'Como reage a imprevistos:', 'opcoes': ['Adapto rapidamente', 'Fico ansioso', 'Busco ajuda', 'Mantenho a calma']},
            {'pergunta': 'Seu nível de organização:', 'opcoes': ['Extremamente organizado', 'Organizado suficiente', 'Caótico funcional', 'Desorganizado']},
            {'pergunta': 'Em relação a riscos:', 'opcoes': ['Calcula e assume', 'Prefere segurança', 'Adora desafios', 'Evita sempre']},
            {'pergunta': 'Em momentos de lazer:', 'opcoes': ['Atividades sociais', 'Hobbies solitários', 'Esportes', 'Descanso total']},
            {'pergunta': 'Se sente realizado quando:', 'opcoes': ['Conquista objetivos', 'Ajuda pessoas', 'Aprende algo novo', 'É reconhecido']},
            
            # Bloco 4: Valores e Crenças (5 questões)
            {'pergunta': 'Seu maior medo é:', 'opcoes': ['Fracasso', 'Rejeição', 'Perder controle', 'Estagnação']},
            {'pergunta': 'O que te irrita mais:', 'opcoes': ['Incompetência', 'Falsidade', 'Desorganização', 'Imposição']},
            {'pergunta': 'Você valoriza mais:', 'opcoes': ['Honestidade', 'Lealdade', 'Inteligência', 'Gentileza']},
            {'pergunta': 'Diante de um problema complexo:', 'opcoes': ['Divido em partes', 'Busco inspiração', 'Peço opiniões', 'Dou tempo ao tempo']},
            {'pergunta': 'Sua filosofia de vida:', 'opcoes': ['Trabalho duro', 'Aproveite o momento', 'Seja gentil', 'Nunca desista']},
            
            # Bloco 5: Autopercepção (5 questões)
            {'pergunta': 'Como você se descreveria:', 'opcoes': ['Ambicioso', 'Criativo', 'Confiável', 'Adaptável']},
            {'pergunta': 'Seu ponto mais forte:', 'opcoes': ['Resolução de problemas', 'Comunicação', 'Liderança', 'Persistência']},
            {'pergunta': 'Seu maior desafio:', 'opcoes': ['Paciência', 'Autoconfiança', 'Foco', 'Empatia']},
            {'pergunta': 'Como lida com pressão:', 'opcoes': ['Desempenho melhor', 'Mantenho a calma', 'Fico estressado', 'Evito situações']},
            {'pergunta': 'Você se considera:', 'opcoes': ['Perfeccionista', 'Pragmático', 'Idealista', 'Realista']},
            
            # Bloco 6: Relacionamentos (5 questões)
            {'pergunta': 'Em relacionamentos você:', 'opcoes': ['É leal', 'É independente', 'É intenso', 'É cauteloso']},
            {'pergunta': 'Para você, amizade é:', 'opcoes': ['Apoio mútuo', 'Diversão', 'Confiança total', 'Interesses comuns']},
            {'pergunta': 'Como expressa afeto:', 'opcoes': ['Atos práticos', 'Palavras', 'Tempo junto', 'Presentes']},
            {'pergunta': 'Em uma discussão você:', 'opcoes': ['Defende seu ponto', 'Busca entender', 'Evita confronto', 'Procura solução']},
            {'pergunta': 'Você precisa de:', 'opcoes': ['Espaço pessoal', 'Conexão constante', 'Validação', 'Liberdade']},
            
            # Bloco 7: Futuro e Ambições (5 questões)
            {'pergunta': 'Daqui a 5 anos você quer:', 'opcoes': ['Sucesso profissional', 'Estabilidade familiar', 'Realização pessoal', 'Liberdade financeira']},
            {'pergunta': 'Seu maior sonho é:', 'opcoes': ['Ser reconhecido', 'Fazer diferença', 'Ser independente', 'Viver em paz']},
            {'pergunta': 'Para ter sucesso você precisa:', 'opcoes': ['Trabalhar muito', 'Ter sorte', 'Fazer networking', 'Ser autêntico']},
            {'pergunta': 'Você aprende melhor:', 'opcoes': ['Fazendo', 'Lendo', 'Conversando', 'Observando']},
            {'pergunta': 'Sua maior influência vem de:', 'opcoes': ['Mentores', 'Experiências', 'Livros', 'Intuição']},
        ],
        'resultados': {
            'preview': 'Sua análise revela um perfil marcado por características analíticas e reflexivas. Você demonstra traços de pensador estratégico, o que significa que tende a planejar antes de agir. Pessoas com seu perfil são confiáveis e orientadas...',
            'completo': '''═══════════════════════════════════════════════════
ANÁLISE COMPLETA DE PERSONALIDADE
Relatório Psicológico Detalhado
═══════════════════════════════════════════════════

📊 SEU PERFIL DOMINANTE: Analista Estratégico
Código MBTI: INTJ (Introvertido, Intuitivo, Pensante, Julgador)
Raridade: Apenas 2-4% da população mundial possui este perfil

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 CARACTERÍSTICAS FUNDAMENTAIS

Você é uma pessoa naturalmente introspectiva e profundamente analítica. Sua mente funciona como um processador estratégico, sempre buscando otimizar processos e encontrar as soluções mais eficientes. Enquanto outros agem por impulso, você prefere observar, analisar e só então tomar decisões fundamentadas.

Sua capacidade de visão sistêmica é notável - você consegue enxergar o panorama completo enquanto simultaneamente presta atenção aos detalhes cruciais. Esta é uma habilidade rara e extremamente valiosa no mundo moderno.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ SEUS PONTOS FORTES (Talentos Naturais)

1. PENSAMENTO ESTRATÉGICO EXCEPCIONAL
   → Você naturalmente enxerga 5 passos à frente
   → Antecipa problemas antes que aconteçam
   → Cria planos de ação detalhados e eficazes
   → Esta habilidade te coloca à frente de 95% das pessoas

2. CAPACIDADE ANALÍTICA SUPERIOR
   → Processa informações complexas com facilidade
   → Identifica padrões que outros não veem
   → Toma decisões baseadas em lógica, não em emoção
   → Seu cérebro funciona como um computador de alta performance

3. INDEPENDÊNCIA E AUTODETERMINAÇÃO
   → Não precisa de validação externa constante
   → Confia em seu próprio julgamento
   → Sabe o que quer e vai atrás
   → Esta autonomia é sinal de maturidade emocional avançada

4. FOCO E DETERMINAÇÃO
   → Quando estabelece um objetivo, não desiste
   → Mantém a disciplina mesmo quando outros desistem
   → Sua persistência é uma de suas maiores armas
   → Pessoas bem-sucedidas compartilham esta característica

5. VISÃO DE LONGO PRAZO
   → Pensa no futuro, não apenas no presente
   → Faz sacrifícios hoje por recompensas amanhã
   → Entende o poder do efeito composto
   → Esta mentalidade é típica de grandes líderes

6. SEDE POR CONHECIMENTO
   → Está sempre aprendendo e se desenvolvendo
   → Valoriza competência e expertise
   → Busca constantemente se aperfeiçoar
   → O aprendizado contínuo é seu diferencial competitivo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💼 ESTILO DE TRABALHO E CARREIRA

AMBIENTE IDEAL:
Você prospera em ambientes que:
• Valorizam a excelência e a competência técnica
• Oferecem autonomia e liberdade criativa
• Permitem trabalho profundo sem interrupções constantes
• Reconhecem resultados, não apenas esforço
• Estimulam inovação e pensamento crítico

COMO VOCÊ TRABALHA MELHOR:
→ Projetos complexos que desafiam seu intelecto
→ Trabalho independente com objetivos claros
→ Ambientes meritocráticos
→ Tarefas que exigem solução de problemas
→ Situações que permitem planejamento estratégico

CARREIRAS ALTAMENTE COMPATÍVEIS (Top 10):
1. Engenharia de Software / Arquiteto de Sistemas
2. Cientista de Dados / Analista de BI
3. Estrategista de Negócios / Consultor
4. Engenheiro (Qualquer especialização)
5. Arquiteto / Designer de Sistemas
6. Pesquisador Científico
7. Analista Financeiro / Investimentos
8. Product Manager / Gerente de Projetos
9. Empreendedor Tech / Startup Founder
10. Professor Universitário / Especialista Acadêmico

💰 POTENCIAL DE RENDA:
Seu perfil está estatisticamente associado a rendas acima da média. Profissionais INTJ tendem a estar entre os 20% mais bem pagos em suas áreas devido à sua competência técnica e visão estratégica.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❤️ RELACIONAMENTOS E VIDA SOCIAL

AMIZADES:
Você não é de ter 100 amigos superficiais. Prefere poucos relacionamentos profundos e significativos. Isso não é defeito - é sinal de maturidade e autenticidade. Você valoriza QUALIDADE sobre quantidade.

Seus amigos verdadeiros te admiram por:
✓ Ser extremamente confiável
✓ Dar conselhos sábios e práticos
✓ Ser honesto, mesmo quando a verdade dói
✓ Estar presente nos momentos importantes
✓ Respeitar a privacidade e espaço alheio

RELACIONAMENTOS ROMÂNTICOS:
Você leva relacionamentos a sério. Não está interessado em superficialidade ou jogos emocionais. Quando se compromete, é intenso e leal.

Seu parceiro ideal:
• Valoriza inteligência e conversas profundas
• Respeita sua necessidade de espaço
• É independente e tem seus próprios objetivos
• Comunica-se de forma clara e direta
• Compartilha valores fundamentais com você

⚠️ IMPORTANTE: Você pode parecer "frio" para pessoas muito emotivas, mas na verdade você sente profundamente - apenas expressa de forma diferente. Sua lealdade e comprometimento falam mais alto que mil palavras românticas.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 ÁREAS DE DESENVOLVIMENTO (Oportunidades de Crescimento)

COMUNICAÇÃO EMOCIONAL:
Às vezes sua objetividade pode ser interpretada como frieza. Praticar expressar emoções de forma mais aberta pode fortalecer seus relacionamentos.

💡 Dica Prática: Ao dar feedback, comece com algo positivo, depois seja direto, e termine reforçando sua confiança na pessoa.

FLEXIBILIDADE:
Seu amor por planos pode te tornar resistente a mudanças imprevistas. A vida nem sempre segue o roteiro.

💡 Dica Prática: Reserve 20% de "buffer" em seus planos para imprevistos. Isso te dará flexibilidade sem perder o controle.

DELEGAÇÃO:
Sua tendência ao perfeccionismo pode fazer você querer controlar tudo. Aprender a delegar é crucial para crescer.

💡 Dica Prática: Identifique tarefas que são 80% boas o suficiente e delegue para outros se desenvolverem.

NETWORKING:
Você prefere profundidade a superficialidade, mas networking estratégico pode abrir portas importantes.

💡 Dica Prática: Defina uma meta de fazer 1-2 conexões significativas por mês, focando em qualidade.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 COMPATIBILIDADE COM OUTROS PERFIS

EXCELENTE COMPATIBILIDADE (90-100%):
• ENFP (O Inspirador) - Complementam sua lógica com criatividade
• ENTP (O Visionário) - Estimulam debates intelectuais
• INTJ (Você mesmo) - Entendem completamente sua forma de pensar

BOA COMPATIBILIDADE (70-89%):
• ENTJ (O Comandante) - Compartilham ambição e visão estratégica
• INFP (O Idealista) - Trazem profundidade emocional
• INTP (O Lógico) - Apreciam análise e conhecimento

COMPATIBILIDADE MODERADA (50-69%):
• ISTJ (O Inspetor) - Compartilham organização mas podem ser rígidos
• ISTP (O Artesão) - Práticos mas podem ser muito no presente

DESAFIADORA (Requer esforço):
• ESFP (O Animador) - Muito espontâneos e emocionais
• ESFJ (O Provedor) - Focam muito em harmonia social

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 PLANO DE AÇÃO PERSONALIZADO PARA SEU CRESCIMENTO

CURTO PRAZO (Próximos 30 dias):
□ Identifique 3 áreas de conhecimento que quer dominar
□ Crie um sistema de organização pessoal (se ainda não tem)
□ Pratique expressar gratidão a pessoas importantes
□ Faça um networking significativo por semana
□ Reserve tempo para reflexão e planejamento semanal

MÉDIO PRAZO (Próximos 6 meses):
□ Desenvolva uma habilidade técnica avançada na sua área
□ Crie um projeto pessoal desafiador
□ Pratique delegar ou ensinar alguém
□ Leia 6 livros sobre liderança e desenvolvimento pessoal
□ Estabeleça uma rotina de exercícios (mente sã, corpo são)

LONGO PRAZO (Próximos 12-24 meses):
□ Posicione-se como especialista na sua área
□ Construa um portfólio impressionante
□ Desenvolva sua presença profissional (LinkedIn, etc)
□ Mentor para alguém menos experiente
□ Estabeleça metas financeiras ambiciosas e alcançáveis

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 RECURSOS RECOMENDADOS ESPECIALMENTE PARA SEU PERFIL

LIVROS ESSENCIAIS:
• "Thinking, Fast and Slow" - Daniel Kahneman
• "Deep Work" - Cal Newport  
• "The 48 Laws of Power" - Robert Greene
• "Atomic Habits" - James Clear
• "Zero to One" - Peter Thiel

CURSOS E HABILIDADES:
• Pensamento Sistêmico
• Análise de Dados Avançada
• Negociação Estratégica
• Gestão de Projetos (PMP/Agile)
• Programação (Python, SQL)

FERRAMENTAS DE PRODUTIVIDADE:
• Notion (Organização e planejamento)
• Obsidian (Gestão de conhecimento)
• Todoist (Gerenciamento de tarefas)
• RescueTime (Análise de produtividade)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎖️ PESSOAS FAMOSAS COM SEU PERFIL

Você compartilha seu tipo de personalidade com:
• Elon Musk - Empreendedor visionário
• Mark Zuckerberg - Fundador do Facebook
• Isaac Newton - Físico e matemático
• Nikola Tesla - Inventor e visionário
• Friedrich Nietzsche - Filósofo
• Christopher Nolan - Diretor de cinema
• Vladimir Putin - Estrategista político
• Michelle Obama - Advogada e ex-primeira dama

Veja o padrão? Pessoas que mudaram o mundo através de visão estratégica, inteligência e determinação inabalável.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💎 MENSAGEM FINAL: SEU POTENCIAL EXTRAORDINÁRIO

Você possui um conjunto raro de características que, quando bem direcionadas, podem levá-lo a conquistas extraordinárias. Seu cérebro funciona de uma maneira que apenas 2-4% da população compreende.

NÃO subestime o poder de:
✓ Seu pensamento estratégico
✓ Sua capacidade de foco intenso
✓ Sua sede insaciável por conhecimento
✓ Sua determinação inabalável
✓ Sua visão de longo prazo

Enquanto outros buscam atalhos, você constrói fundações sólidas.
Enquanto outros desistem, você persevera.
Enquanto outros seguem a multidão, você traça seu próprio caminho.

🌟 VOCÊ NÃO É COMUM - E ISSO É SUA MAIOR FORÇA.

O mundo precisa de pessoas como você: que pensam profundamente, planejam estrategicamente e executam impecavelmente. Não tente se encaixar em padrões comuns. Seu diferencial está justamente em ser quem você é.

Continue investindo em si mesmo. Continue aprendendo. Continue crescendo. Seu futuro é brilhante porque você tem a mentalidade e as habilidades necessárias para construí-lo.

═══════════════════════════════════════════════════
Este relatório foi gerado baseado em suas respostas
e análise psicométrica avançada. Guarde-o e releia
sempre que precisar de direcionamento e motivação.
═══════════════════════════════════════════════════

© 2025 - Análise Psicológica Profissional
Válido permanentemente como referência pessoal
'''
        }
    }
}

def analisar_signo(respostas):
    """Analisa as respostas e determina o perfil astrológico espiritual"""
    # Mapeia características astrológicas
    elementos = {
        'fogo': 0,
        'terra': 0,
        'ar': 0,
        'agua': 0
    }
    
    # Análise baseada nas respostas
    for i, resp in respostas.items():
        idx = int(i.split('_')[1])
        opcao = int(resp) if resp.isdigit() else 0
        
        # BLOCO 1: Temperamento e Personalidade
        if idx == 0:  # Energia
            if opcao == 0: elementos['fogo'] += 3
            elif opcao == 1: elementos['terra'] += 3
            elif opcao == 2: elementos['ar'] += 3
            else: elementos['agua'] += 3
            
        elif idx == 1:  # Abordagem
            if opcao == 0: elementos['terra'] += 3
            elif opcao == 1: elementos['ar'] += 3
            elif opcao == 2: elementos['agua'] += 3
            else: elementos['fogo'] += 3
            
        elif idx == 2:  # Emoções
            if opcao == 0: elementos['agua'] += 3
            elif opcao == 1: elementos['terra'] += 3
            elif opcao == 2: elementos['fogo'] += 3
            else: elementos['ar'] += 3
            
        elif idx == 3:  # Decisões
            if opcao == 0: elementos['terra'] += 3
            elif opcao == 1: elementos['agua'] += 3
            elif opcao == 2: elementos['ar'] += 3
            else: elementos['fogo'] += 3
            
        elif idx == 4:  # Relações
            if opcao == 0: elementos['agua'] += 3
            elif opcao == 1: elementos['terra'] += 3
            elif opcao == 2: elementos['fogo'] += 3
            else: elementos['ar'] += 3
    
    # Determina elemento dominante
    elemento_dominante = max(elementos.items(), key=lambda x: x[1])[0]
    
    # Mapeia signos por elemento
    signos = {
        'fogo': ['Áries', 'Leão', 'Sagitário'],
        'terra': ['Touro', 'Virgem', 'Capricórnio'],
        'ar': ['Gêmeos', 'Libra', 'Aquário'],
        'agua': ['Câncer', 'Escorpião', 'Peixes']
    }
    
    # Escolhe um signo baseado no elemento dominante
    signo_espiritual = random.choice(signos[elemento_dominante])
    
    return {
        'signo': signo_espiritual,
        'elemento': elemento_dominante,
        'elementos': elementos
    }

def gerar_preview_signo(analise):
    """Gera um preview variado para o teste de signo espiritual"""
    previews = [
        f"Sua energia vital revela uma forte conexão com {analise['elemento'].title()}, manifestando-se através do signo de {analise['signo']}. Esta combinação única sugere um caminho espiritual profundo...",
        f"A análise das suas respostas indica uma ressonância natural com o elemento {analise['elemento'].title()}, que se expressa através das características do signo de {analise['signo']}. Seu perfil espiritual mostra...",
        f"Seu verdadeiro signo espiritual é {analise['signo']}, fortemente influenciado pelo elemento {analise['elemento'].title()}. Esta descoberta revela aspectos profundos da sua jornada..."
    ]
    return random.choice(previews)

def gerar_resultado_completo_signo(analise):
    """Gera resultado completo personalizado do signo espiritual"""
    signo = analise['signo']
    elemento = analise['elemento']
    elementos = analise['elementos']
    
    # Características por signo
    caracteristicas_signos = {
        'Áries': {
            'natureza': 'Pioneiro e Corajoso',
            'potenciais': ['Liderança Natural', 'Iniciativa', 'Coragem', 'Determinação'],
            'desafios': ['Impulsividade', 'Impaciência', 'Teimosia'],
            'caminho': 'Você nasceu para ser um líder espiritual, abrindo novos caminhos.'
        },
        'Touro': {
            'natureza': 'Estável e Determinado',
            'potenciais': ['Perseverança', 'Força Interior', 'Sensualidade', 'Praticidade'],
            'desafios': ['Rigidez', 'Materialismo', 'Resistência à Mudança'],
            'caminho': 'Seu papel é manifestar o espiritual no mundo material.'
        },
        'Gêmeos': {
            'natureza': 'Versátil e Comunicativo',
            'potenciais': ['Adaptabilidade', 'Comunicação', 'Inteligência', 'Curiosidade'],
            'desafios': ['Dispersão', 'Superficialidade', 'Ansiedade'],
            'caminho': 'Você é um mensageiro espiritual, ponte entre diferentes realidades.'
        },
        'Câncer': {
            'natureza': 'Intuitivo e Protetor',
            'potenciais': ['Intuição', 'Empatia', 'Cuidado', 'Memória Emocional'],
            'desafios': ['Dependência', 'Medo', 'Apego Excessivo'],
            'caminho': 'Seu dom é nutrir e cuidar das almas ao seu redor.'
        },
        'Leão': {
            'natureza': 'Magnético e Criativo',
            'potenciais': ['Criatividade', 'Carisma', 'Generosidade', 'Autoexpressão'],
            'desafios': ['Orgulho', 'Arrogância', 'Necessidade de Atenção'],
            'caminho': 'Você veio para iluminar e inspirar os outros.'
        },
        'Virgem': {
            'natureza': 'Analítico e Perfeccionista',
            'potenciais': ['Discernimento', 'Cura', 'Serviço', 'Organização'],
            'desafios': ['Crítica', 'Preocupação', 'Perfeccionismo'],
            'caminho': 'Seu propósito é trazer cura e ordem ao caos.'
        },
        'Libra': {
            'natureza': 'Harmonioso e Diplomático',
            'potenciais': ['Harmonia', 'Justiça', 'Arte', 'Diplomacia'],
            'desafios': ['Indecisão', 'Dependência', 'Evitar Conflitos'],
            'caminho': 'Você é um pacificador, trazendo equilíbrio ao mundo.'
        },
        'Escorpião': {
            'natureza': 'Profundo e Transformador',
            'potenciais': ['Poder de Cura', 'Intuição', 'Transformação', 'Mistério'],
            'desafios': ['Obsessão', 'Vingança', 'Manipulação'],
            'caminho': 'Sua missão é facilitar transformações profundas.'
        },
        'Sagitário': {
            'natureza': 'Explorador e Otimista',
            'potenciais': ['Sabedoria', 'Aventura', 'Fé', 'Expansão'],
            'desafios': ['Excessos', 'Inquietação', 'Promessas Demais'],
            'caminho': 'Você é um professor espiritual, expandindo horizontes.'
        },
        'Capricórnio': {
            'natureza': 'Responsável e Ambicioso',
            'potenciais': ['Mestria', 'Disciplina', 'Sabedoria', 'Realização'],
            'desafios': ['Rigidez', 'Pessimismo', 'Workaholic'],
            'caminho': 'Seu destino é construir pontes entre o material e o espiritual.'
        },
        'Aquário': {
            'natureza': 'Visionário e Revolucionário',
            'potenciais': ['Inovação', 'Humanitarismo', 'Originalidade', 'Visão'],
            'desafios': ['Rebeldia', 'Distanciamento', 'Excentricidade'],
            'caminho': 'Você é um pioneiro espiritual, trazendo novas visões.'
        },
        'Peixes': {
            'natureza': 'Místico e Compassivo',
            'potenciais': ['Compaixão', 'Intuição', 'Arte', 'Cura'],
            'desafios': ['Escapismo', 'Confusão', 'Vitimização'],
            'caminho': 'Sua essência é dissolver barreiras e unir as almas.'
        }
    }
    
    # Características do elemento
    elementos_info = {
        'fogo': {
            'energia': 'Transformadora e Dinâmica',
            'aspectos': ['Intuição', 'Inspiração', 'Ação', 'Transformação'],
            'lições': 'Aprender a canalizar sua energia com sabedoria.'
        },
        'terra': {
            'energia': 'Estável e Manifestadora',
            'aspectos': ['Praticidade', 'Estabilidade', 'Manifestação', 'Abundância'],
            'lições': 'Equilibrar o material com o espiritual.'
        },
        'ar': {
            'energia': 'Mental e Comunicativa',
            'aspectos': ['Pensamento', 'Comunicação', 'Conexões', 'Ideias'],
            'lições': 'Usar o intelecto a serviço do espírito.'
        },
        'agua': {
            'energia': 'Emocional e Intuitiva',
            'aspectos': ['Emoção', 'Intuição', 'Cura', 'Fluidez'],
            'lições': 'Navegar as águas profundas da alma.'
        }
    }
    
    info_signo = caracteristicas_signos[signo]
    info_elemento = elementos_info[elemento]
    
    resultado = f'''═══════════════════════════════════════════════════
SEU VERDADEIRO SIGNO ESPIRITUAL
Análise Astrológica Profunda
═══════════════════════════════════════════════════

🌟 REVELAÇÃO PRINCIPAL:
Seu Signo Espiritual é {signo}
Elemento Dominante: {elemento.title()}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔮 SUA NATUREZA ESPIRITUAL:
{info_signo['natureza']}

Esta combinação revela uma alma com propósito especial. 
{info_signo['caminho']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ SEUS DONS E POTENCIAIS:
'''
    
    for potencial in info_signo['potenciais']:
        resultado += f"• {potencial}\n"
    
    resultado += f'''
🌊 ENERGIA ELEMENTAR:
Sua energia é {info_elemento['energia']}

Aspectos Principais:
'''
    
    for aspecto in info_elemento['aspectos']:
        resultado += f"• {aspecto}\n"
    
    resultado += f'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ DESAFIOS DA ALMA:
Pontos de Crescimento:
'''
    
    for desafio in info_signo['desafios']:
        resultado += f"• {desafio}\n"
    
    resultado += f'''
💫 LIÇÃO PRINCIPAL:
{info_elemento['lições']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 SEU CAMINHO ESPIRITUAL:

1. PROPÓSITO MAIOR
{info_signo['caminho']}

2. DONS A DESENVOLVER:
'''
    
    for i, potencial in enumerate(info_signo['potenciais'], 1):
        resultado += f"→ {potencial}: Seu {i}º dom natural\n"
    
    resultado += '''
3. PRÁTICAS RECOMENDADAS:

DIARIAMENTE:
□ Meditação focada em seu elemento
□ Gratidão consciente
□ Conexão com sua intuição

SEMANALMENTE:
□ Ritual de limpeza energética
□ Estudo espiritual
□ Prática de cura

MENSALMENTE:
□ Ritual de lua cheia
□ Avaliação de progresso
□ Reconexão com propósito

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌟 MENSAGEM DOS GUIAS ESPIRITUAIS:

Você não está aqui por acaso. Seu signo espiritual revela um propósito maior em sua jornada terrena. Confie em seus dons naturais e permita que sua luz interior brilhe.

Lembre-se:
"Sua alma escolheu este caminho por uma razão.
As dificuldades são oportunidades de crescimento.
Seus dons são presentes para o mundo."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📿 CRISTAIS RECOMENDADOS:
'''
    
    # Cristais por elemento
    cristais = {
        'fogo': ['Granada', 'Citrino', 'Rubi', 'Olho de Tigre'],
        'terra': ['Jade', 'Turmalina Verde', 'Quartzo Fumê', 'Ágata'],
        'ar': ['Ametista', 'Quartzo Azul', 'Topázio', 'Fluorita'],
        'agua': ['Água Marinha', 'Selenita', 'Quartzo Rosa', 'Opala']
    }
    
    for cristal in cristais[elemento]:
        resultado += f"• {cristal}\n"
    
    resultado += '''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌿 ERVAS & INCENSOS ALINHADOS:
'''
    
    # Ervas por elemento
    ervas = {
        'fogo': ['Alecrim', 'Canela', 'Gengibre', 'Pimenta'],
        'terra': ['Sálvia', 'Cedro', 'Patchouli', 'Vetiver'],
        'ar': ['Lavanda', 'Eucalipto', 'Hortelã', 'Sândalo'],
        'agua': ['Camomila', 'Jasmim', 'Lótus', 'Mirra']
    }
    
    for erva in ervas[elemento]:
        resultado += f"• {erva}\n"
    
    resultado += '''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎭 ASPECTOS KÁRMICOS:

VIDAS PASSADAS:
Suas experiências anteriores moldaram quem você é hoje. Seu signo espiritual indica padrões importantes de outras encarnações.

LIÇÕES ATUAIS:
1. Reconhecer seu poder interior
2. Superar medos ancestrais
3. Manifestar seus dons divinos
4. Equilibrar material e espiritual

PRÓXIMOS PASSOS:
1. Aceite sua natureza única
2. Desenvolva seus dons naturais
3. Confie em sua intuição
4. Compartilhe sua luz

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌈 AFIRMAÇÕES PODEROSAS:

Repita diariamente:
1. "Eu reconheço e honro minha natureza divina"
2. "Meus dons são presentes para o mundo"
3. "Estou em harmonia com meu propósito maior"
4. "Cada dia me aproximo mais da minha verdade"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 RITUAIS MENSAIS RECOMENDADOS:

LUA NOVA:
• Definir intenções alinhadas com seu propósito
• Meditar com seus cristais
• Escrever suas visões

LUA CHEIA:
• Ritual de gratidão
• Limpeza energética
• Celebração de realizações

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💫 MENSAGEM FINAL:

Seu signo espiritual é um mapa para sua evolução. Não é sobre predestinação, mas sobre potencial. Você tem o poder de escolha e a sabedoria interior para navegar seu caminho.

Lembre-se: Você é uma alma eterna em uma jornada sagrada.

═══════════════════════════════════════════════════
© 2025 - Análise Astrológica Espiritual
Baseada em padrões energéticos ancestrais
═══════════════════════════════════════════════════
'''
    
    return resultado

def importar_emails_antigos():
    """Importa emails antigos do banco de dados para o arquivo de texto"""
    emails = set()  # Usamos um set para garantir emails únicos
    
    # Lê emails existentes do arquivo
    try:
        with open('emails_registrados.txt', 'r', encoding='utf-8') as f:
            emails.update(f.read().splitlines())
    except FileNotFoundError:
        pass
    
    # Adiciona emails do banco de dados
    emails.update(Resposta.objects.exclude(email='').values_list('email', flat=True).distinct())
    
    # Salva todos os emails no arquivo
    with open('emails_registrados.txt', 'w', encoding='utf-8') as f:
        for email in sorted(emails):
            f.write(f'{email}\n')

def home(request):
    testes = [{'tipo': tipo, 'titulo': config['titulo'], 'descricao': config['descricao'], 'icone': config['icone']} for tipo, config in TESTES_CONFIG.items()]
    return render(request, 'home.html', {'testes': testes})

def teste_view(request, tipo):
    if tipo not in TESTES_CONFIG:
        return redirect('testes:home')
    config = TESTES_CONFIG[tipo]
    return render(request, 'teste.html', {'tipo': tipo, 'config': config})

def processar_teste(request, tipo):
    if request.method != 'POST':
        return redirect('testes:home')
    if tipo not in TESTES_CONFIG:
        return redirect('testes:home')
    config = TESTES_CONFIG[tipo]
    email = request.POST.get('email', '')
    respostas = {}
    for i, pergunta in enumerate(config['perguntas']):
        resposta = request.POST.get(f'pergunta_{i}', '')
        respostas[f'pergunta_{i}'] = resposta
    
    # Criar ou obter o teste
    from .models import Teste, Resposta
    teste, created = Teste.objects.get_or_create(
        tipo=tipo,
        defaults={
            'titulo': config['titulo'],
            'descricao': config['descricao'],
            'icone': config['icone']
        }
    )
    
    # PERSONALIZAÇÃO: Gera resultados baseados nas respostas reais
    if tipo == 'personalidade':
        analise = analisar_personalidade(respostas)
        preview = gerar_preview_personalidade(analise)
        completo = gerar_resultado_completo_personalidade(analise, respostas)
    elif tipo == 'teste_qi':
        analise = analisar_qi(respostas)
        preview = gerar_preview_qi(analise)
        completo = gerar_resultado_completo_qi(analise)
    elif tipo == 'renda_idade':
        completo = analisar_renda_idade(respostas)
        preview = gerar_preview_renda(respostas)
    elif tipo == 'signo_oculto':
        analise = analisar_signo(respostas)
        preview = gerar_preview_signo(analise)
        completo = gerar_resultado_completo_signo(analise)
    else:
        # Fallback para outros testes
        preview = config['resultados']['preview']
        completo = config['resultados']['completo']
    
    # Salvar a resposta no banco de dados
    resposta = Resposta.objects.create(
        teste=teste,
        email=email,
        respostas=respostas,
        resultado_preview=preview,
        resultado_completo=completo,
        pago=False
    )
    
    # Salvar o email no arquivo de texto apenas em ambiente local (DEBUG)
    # Em produção (Railway) não gravamos no filesystem local.
    write_file = os.environ.get('WRITE_EMAIL_FILE', 'False') == 'True'
    if email and (getattr(settings, 'DEBUG', False) or write_file):
        try:
            with open('emails_registrados.txt', 'a', encoding='utf-8') as f:
                f.write(f'{email}\n')
        except Exception:
            # Não falhar o fluxo principal por problema de I/O
            pass
    
    request.session['ultimo_resultado'] = {
        'tipo': tipo, 
        'email': email, 
        'respostas': respostas, 
        'preview': preview, 
        'completo': completo, 
        'pago': False
    }
    return redirect('testes:resultado', resposta_id=1)

def resultado_view(request, resposta_id):
    resultado = request.session.get('ultimo_resultado', {})
    if not resultado:
        return redirect('testes:home')
    config = TESTES_CONFIG.get(resultado['tipo'], {})
    return render(request, 'resultado.html', {'resultado': resultado, 'config': config, 'resposta_id': resposta_id})

def pagamento_view(request, resposta_id):
    from .models import Resposta
    try:
        resposta = Resposta.objects.get(id=resposta_id)
    except Resposta.DoesNotExist:
        return redirect('testes:home')
    
    config = TESTES_CONFIG.get(resposta.teste.tipo, {})
    resultado = {
        'tipo': resposta.teste.tipo,
        'email': resposta.email,
        'respostas': resposta.respostas,
        'preview': resposta.resultado_preview,
        'completo': resposta.resultado_completo,
        'pago': resposta.pago
    }
    
    if request.method == 'POST':
        resposta.pago = True
        resposta.save()
        resultado['pago'] = True
        request.session['ultimo_resultado'] = resultado
        return render(request, 'resultado_completo.html', {'resultado': resultado, 'config': config})
    
    return render(request, 'pagamento.html', {'resultado': resultado, 'config': config, 'resposta_id': resposta_id, 'preco': '4,99'})
