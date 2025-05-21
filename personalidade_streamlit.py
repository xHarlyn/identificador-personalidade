import streamlit as st

def identificador_de_personalidade():
    # Configurando o estilo da página
    st.set_page_config(
        page_title="Identificador de Personalidade",
        page_icon="🧠",
        layout="centered"
    )
    
    # Estilo personalizado
    st.markdown("""
    <style>
    .main {
        background-color: #1e2a3a;
        color: #f0f4f8;
    }
    .stButton > button {
        width: 100%;
        background-color: #0078d4;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 4px;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #005da6;
    }
    div[data-testid="stForm"] {
        background-color: #19273a;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Inicializando o estado da sessão, se ainda não existir
    if 'estagio' not in st.session_state:
        st.session_state.estagio = 'inicio'
    if 'nome' not in st.session_state:
        st.session_state.nome = ''
    if 'resultado' not in st.session_state:
        st.session_state.resultado = ''
    if 'mostrar_final' not in st.session_state:
        st.session_state.mostrar_final = False
    
    # Tela inicial
    if st.session_state.estagio == 'inicio':
        st.title("IDENTIFICADOR DE PERSONALIDADE")
        
        # Formulário de nome
        with st.form("form_nome"):
            nome = st.text_input("Digite seu nome:")
            submit_button = st.form_submit_button("Começar")
            
            if submit_button:
                if nome.strip():
                    st.session_state.nome = nome
                    st.session_state.estagio = 'pergunta1'
                    st.rerun()
                else:
                    st.error("Por favor, digite seu nome!")
    
    # Pergunta 1
    elif st.session_state.estagio == 'pergunta1':
        st.title(f"Okay {st.session_state.nome}, agora iremos começar!")
        st.header("Dentre estas 3 opções, como você descreveria sua pessoa?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("1- Humilde"):
                st.session_state.a1 = 1
                st.session_state.estagio = 'pergunta2'
                st.rerun()
        
        with col2:
            if st.button("2- Especial"):
                st.session_state.a1 = 2
                st.session_state.estagio = 'pergunta3'  # Vai para defeitos se escolher Especial
                st.rerun()
        
        with col3:
            if st.button("3- Egoísta"):
                st.session_state.a1 = 3
                st.session_state.estagio = 'pergunta5'  # Vai para desejos se escolher Egoísta
                st.rerun()
    
    # Pergunta 2 (10 mil reais)
    elif st.session_state.estagio == 'pergunta2':
        st.header("O que você faria se recebesse 10 mil reais por engano?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("1- Guardar, para caso o dono te procurasse."):
                st.session_state.a3 = 1
                st.session_state.estagio = 'pergunta3'  # Vai para defeitos
                st.rerun()
        
        with col2:
            if st.button("2- Gastar, não é culpa sua terem cometido este erro."):
                st.session_state.a3 = 2
                st.session_state.estagio = 'pergunta4'  # Vai para traição
                st.rerun()
        
        with col3:
            if st.button("3- Devolver, nunca se sabe quando pode acontecer com você."):
                st.session_state.a3 = 3
                st.session_state.estagio = 'pergunta5'  # Vai para desejos
                st.rerun()
    
    # Pergunta 3 (Defeitos)
    elif st.session_state.estagio == 'pergunta3':
        st.header('Qual desses "Defeitos" é mais plausível de você ter?')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("1- Perfeccionismo"):
                st.session_state.a5 = 1
                # Se veio da pergunta 1 com humilde ou da especial, vai para traição
                if st.session_state.a1 in [1, 2]:
                    st.session_state.estagio = 'pergunta4'
                    st.rerun()
        
        with col2:
            if st.button("2- Bondade"):
                st.session_state.a5 = 2
                # Se veio do caminho humilde e guardar, vai direto para resultado
                if st.session_state.a1 == 1 and st.session_state.a3 == 1:
                    st.session_state.resultado = f'Parabéns, {st.session_state.nome}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.'
                    st.session_state.estagio = 'resultado'
                    st.rerun()
                # Se veio do caminho especial, vai para pergunta 2
                elif st.session_state.a1 == 2:
                    st.session_state.estagio = 'pergunta2'
                    st.rerun()
        
        with col3:
            if st.button("3- Empatia"):
                st.session_state.a5 = 3
                # Se veio do caminho humilde e guardar, vai para desejos
                if st.session_state.a1 == 1 and st.session_state.a3 == 1:
                    st.session_state.estagio = 'pergunta5'
                    st.rerun()
                # Se veio do caminho especial, vai para desejos
                elif st.session_state.a1 == 2:
                    st.session_state.estagio = 'pergunta5'
                    st.rerun()
    
    # Pergunta 4 (Traição)
    elif st.session_state.estagio == 'pergunta4':
        st.header("Como você reagiria em caso de traição?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("1- Compreensivo"):
                st.session_state.a2 = 1
                st.session_state.resultado = f'Realmente, {st.session_state.nome}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: Para quem você está tentando se provar?'
                st.session_state.estagio = 'resultado'
                st.rerun()
        
        with col2:
            if st.button("2- Agressivo"):
                st.session_state.a2 = 2
                st.session_state.resultado = f'Então, violência é a única solução, {st.session_state.nome}?\nPensava que sua índole fosse levá-lo a decisões diferentes, mas quem estamos tentando enganar? kkkk'
                st.session_state.estagio = 'resultado'
                st.rerun()
        
        with col3:
            if st.button("3- Apático"):
                st.session_state.a2 = 3
                st.session_state.resultado = f'Admirável ou perturbador?\nA verdade é que ninguém é mais importante que nós mesmos, não é mesmo {st.session_state.nome}?'
                st.session_state.estagio = 'resultado'
                st.rerun()
    
    # Pergunta 5 (Desejos)
    elif st.session_state.estagio == 'pergunta5':
        st.header("Se pudesse realizar um desejo, qual seria?")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("1- Fim da Pobreza."):
                st.session_state.a4 = 1
                st.session_state.resultado = f'Parabéns, {st.session_state.nome}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.'
                st.session_state.estagio = 'resultado'
                st.rerun()
        
        with col2:
            if st.button("2- A Cura do Câncer."):
                st.session_state.a4 = 2
                st.session_state.resultado = f'{st.session_state.nome},\nFico me perguntando se todas essas perguntas fossem reais a ponto de sua vida depender disso, como você reagiria ao saber que existem pessoas iguais a você por aí?'
                st.session_state.estagio = 'resultado'
                st.rerun()
        
        with col3:
            if st.button("3- Mais 3 desejos."):
                st.session_state.a4 = 3
                st.session_state.resultado = f'Por que será que eu não esperava mais de você, {st.session_state.nome}?'
                st.session_state.estagio = 'resultado'
                st.rerun()
    
    # Caso especial para a soma 5 do caminho 2 (especial + bondade + guardar)
    elif st.session_state.estagio == 'pergunta2_especial':
        # Tratar caso especial de quem escolheu o caminho da Bondade após Especial
        if st.session_state.a1 == 2 and st.session_state.a5 == 2 and 'a3' in st.session_state:
            if st.session_state.a3 == 1:  # Guardar
                st.session_state.resultado = f'Realmente, {st.session_state.nome}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: A quem você está tentando se enganar?'
                st.session_state.estagio = 'resultado'
                st.rerun()
    
    # Tela de Resultado
    elif st.session_state.estagio == 'resultado':
        st.title("Resultado")
        
        # Container estilizado para o resultado
        with st.container():
            resultado_texto = st.session_state.resultado if not st.session_state.mostrar_final else "Eaí? Se divertiu? Vamos tentar novamente?"
            st.markdown(f"""
            <div style="background-color: #19273a; padding: 30px; border-radius: 10px; margin: 20px 0;">
                <p style="font-size: 18px; line-height: 1.6;">{resultado_texto}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if not st.session_state.mostrar_final:
                if st.button("Recomeçar"):
                    st.session_state.mostrar_final = True
                    st.rerun()
            else:
                # Timer para voltar ao início após 3 segundos
                import time
                time.sleep(3)
                # Resetar todos os estados
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.session_state.estagio = 'inicio'
                st.rerun()

# Iniciar o aplicativo
if __name__ == "__main__":
    identificador_de_personalidade()