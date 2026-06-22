import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import datetime
import plotly.express as px
import json

# 1. Configuração de Página Imersiva
st.set_page_config(page_title="CYBER-PHYSICAL SHIELD", page_icon="🛡️", layout="wide")

# ==============================================================================
# 🎛️ INTERFACE PREMIUM ULTRA-WIDE SCADA - MAX SUBTITLE GLOW EDIT
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700;800&family=JetBrains+Mono:wght=400;700&display=swap');
    
    /* Fundo Dark Industrial absoluto */
    .main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #090a0f !important;
        background-image: 
            linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px) !important;
        background-size: 20px 20px !important;
    }

    /* Tipografia Industrial de Alta Performance */
    h1, h2, h4, h5, h6, p, span, label, .stMarkdown, [data-testid="stWidgetLabel"] p {
        font-family: 'Inter', sans-serif !important;
        color: #f1f5f9 !important;
        font-weight: 500 !important;
    }

    /* Subtítulos dos Blocos em Caixa Alta */
    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #f1f5f9 !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    /* TÍTULO E CONTAINER DO LOGO */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 30px;
        padding-top: 15px;
        margin-bottom: 5px;
    }

    .huge-nuclear-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        letter-spacing: -0.5px !important;
        text-transform: uppercase !important;
    }
    
    /* ⚡ SUBTÍTULO ULTRA AMPLIFICADO: FONTE DA CARCAÇA + NEON EXTRA BRILHO */
    .huge-nuclear-subtitle {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1.4rem !important; /* Deixando gigante pra dar o impacto que você quer */
        color: #ccff00 !important;    /* Amarelo Fluorescente Radioativo */
        text-align: center !important;
        letter-spacing: 1.5px !important;
        margin-bottom: 35px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        text-shadow: 0 0 15px rgba(204, 255, 0, 0.6) !important; /* Glow tunado */
    }

    /* Dominação do espaço das abas */
    div[data-testid="stTabs"] [data-baseweb="tab-list"] {
        width: 100% !important;
        display: flex !important;
    }
    
    div[data-testid="stTabs"] button {
        flex-grow: 1 !important;
        text-align: center !important;
        font-weight: 600 !important;
    }

    /* Cards do Console */
    div[data-testid="stColumn"] {
        background: #11131c !important;
        border: 1px solid #1e2235 !important;
        border-radius: 8px !important;
        padding: 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2) !important;
    }

    /* Botões */
    .stButton > button, div[data-testid="stFormSubmitButton"] > button {
        background-color: #1e2235 !important;
        color: #ffffff !important;
        border: 1px solid #333a56 !important;
        border-radius: 6px !important;
        padding: 8px 16px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        transition: all 0.15s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        background-color: #2a304d !important;
        border-color: #47527a !important;
    }

    .stButton > button[data-testid="stBaseButton-primary"] {
        background-color: #dc2626 !important;
        color: #ffffff !important;
        border: 1px solid #991b1b !important;
    }
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        background-color: #b91c1c !important;
    }

    /* Responsividade Dinâmica */
    @media (max-width: 1366px) {
        [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 1.45rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
        }
        .huge-nuclear-title { font-size: 1.9rem !important; }
        .huge-nuclear-subtitle { font-size: 1.15rem !important; } /* Reescalado proporcionalmente */
        .header-container svg {
            width: 90px !important;
            height: 90px !important;
        }
    }

    @media (min-width: 1367px) {
        [data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 2.1rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 🛡️ CABEÇALHO COM LOGO REESCALADO (130px)
st.markdown("""
    <div class="header-container">
        <svg width="130" height="130" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 0 15px #3b82f6);">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="#3b82f6" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12 8v4M12 16h.01" stroke="#3b82f6" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div class="huge-nuclear-title">CYBER-PHYSICAL SHIELD • CONSOLE DE SEGURANÇA</div>
    </div>
""", unsafe_allow_html=True)
st.markdown('<div class="huge-nuclear-subtitle">MONITORAMENTO DE ATIVOS CRÍTICOS & PROSPECÇÃO PREDITIVA DE FALHAS</div>', unsafe_allow_html=True)

if 'historico_auditoria' not in st.session_state:
    st.session_state.historico_auditoria = []

# Callbacks de Estado
def forcar_estresse_critico():
    st.session_state.sensor_air = 34.5
    st.session_state.sensor_proc = 44.5
    st.session_state.sensor_rpm = 2750
    st.session_state.sensor_torque = 78.5
    st.session_state.sensor_wear = 245

def resetar_para_minimo():
    st.session_state.sensor_air = 22.0
    st.session_state.sensor_proc = 32.0
    st.session_state.sensor_rpm = 1100
    st.session_state.sensor_torque = 3.0
    st.session_state.sensor_wear = 0

def executar_mitigacao_automatica():
    st.session_state.sensor_rpm = 1250
    st.session_state.sensor_torque = 14.2
    st.session_state.sensor_air = 24.0
    st.session_state.sensor_proc = 34.0
    
    st.session_state.historico_auditoria.append({
        "Timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
        "Temp Ar (°C)": 24.0, "RPM": 1250, "Torque": 14.2, 
        "Status": "MITIGAÇÃO OPERACIONAL ATIVA", "Confiança": "100.0% (CPS-LOOP)"
    })
    st.toast("⚡ PROTOCOLO CPS ATIVADO: Parâmetros reajustados para zona de segurança!", icon="🤖")

if 'sensor_air' not in st.session_state:
    resetar_para_minimo()

# Alerta Sonoro
def tocar_sirene_militar_ultra():
    st.components.v1.html("""
        <div style="background: #2d1418; padding: 12px; border-radius: 6px; border: 1px solid #ef4444; text-align: center;">
            <span style="color: #fca5a5; font-weight: 600; font-family: 'JetBrains Mono', monospace; font-size: 13px;">
                🚨 ALERTA ACÚSTICO DE ANOMALIA ESTRUTURAL ATIVADO NO SISTEMA
            </span>
            <br>
            <button onclick="pararSirene()" style="margin-top: 8px; background: #dc2626; color: white; border: none; padding: 5px 14px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 11px;">
                MUTE MANUAL
            </button>
        </div>
        <script>
            var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            var osc = audioCtx.createOscillator(); osc.type = 'sawtooth'; osc.frequency.setValueAtTime(440, audioCtx.currentTime); 
            var lfo = audioCtx.createOscillator(); lfo.type = 'sine'; lfo.frequency.setValueAtTime(2.0, audioCtx.currentTime); 
            var lfoGain = audioCtx.createGain(); lfoGain.gain.setValueAtTime(150, audioCtx.currentTime); 
            var mainGain = audioCtx.createGain(); mainGain.gain.setValueAtTime(0.12, audioCtx.currentTime); 
            lfo.connect(lfoGain); lfoGain.connect(osc.frequency); osc.connect(mainGain); mainGain.connect(audioCtx.destination); 
            osc.start(); lfo.start(); window.oscGlobal = osc; window.lfoGlobal = lfo;
            function pararSirene() { if(window.oscGlobal) window.oscGlobal.stop(); if(window.lfoGlobal) window.lfoGlobal.stop(); }
        </script>
    """, height=105)

@st.cache_data
def carregar_e_treinar_supremo():
    df = pd.read_csv("predictive_maintenance.csv")
    features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    X = df[features]
    y = df['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(random_state=42, n_estimators=120, max_depth=12)
    modelo.fit(X_train, y_train)
    acuracia = accuracy_score(y_test, modelo.predict(X_test)) * 100
    cm = confusion_matrix(y_test, modelo.predict(X_test))
    return modelo, X, acuracia, cm, df

try:
    modelo, X, acuracia_real, matriz_confusao, df_original = carregar_e_treinar_supremo()
    
    aba_painel, aba_analytics, aba_explorer, aba_logs, aba_api = st.tabs([
        "📡 TELEMETRIA EM TEMPO REAL", "📊 CORE METRICS DA I.A.", "🔍 DATA INVENTÁRIO", "📋 HISTÓRICO DE LOGS", "🌐 INDUSTRIAL API GATEWAY"
    ])
    
    with aba_painel:
        col1, col2 = st.columns([1, 1.3])
        with col1:
            st.subheader("📊 Vetores Cinéticos de Entrada")
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1: st.button("⚡ SIMULAR SOBRECARGA", on_click=forcar_estresse_critico, type="primary")
            with btn_col2: st.button("❄️ ESTABILIZAR SISTEMA", on_click=resetar_para_minimo, type="secondary")
            
            st.markdown("<br>", unsafe_allow_html=True)
            air_temp_c = st.slider("Temperatura Ambiente (°C)", 22.0, 35.0, key="sensor_air", step=0.1)
            proc_temp_c = st.slider("Temperatura do Processo (°C)", 32.0, 45.0, key="sensor_proc", step=0.1)
            rot_speed = st.slider("Rotação do Eixo (RPM)", 1100, 2800, key="sensor_rpm")
            torque = st.slider("Torque Aplicado (Nm)", 3.0, 80.0, key="sensor_torque", step=0.1)
            tool_wear = st.slider("Desgaste da Broca (Minutos)", 0, 250, key="sensor_wear")
            st.progress(tool_wear / 250)
            
            air_temp_k = air_temp_c + 273.15
            proc_temp_k = proc_temp_c + 273.15
            
        with col2:
            st.subheader("🧠 Diagnóstico Preditivo de Falha")
            dados_atuais = pd.DataFrame([[air_temp_k, proc_temp_k, rot_speed, torque, tool_wear]], columns=X.columns)
            predicao = modelo.predict(dados_atuais)[0]
            prob_final = modelo.predict_proba(dados_atuais)[0][predicao] * 100
            status = "SISTEMA SEGURO" if predicao == 0 else "FALHA IMINENTE"
            
            c1, c2 = st.columns(2)
            if predicao == 0:
                c1.metric("ESTADO DO HARDWARE", "NOMINAL ✅")
                c2.metric("CONFIANÇA PREDITIVA", f"{prob_final:.2f}%")
                st.success("✔️ Assinatura operacional estável. O vetor se enquadra nos parâmetros de tolerância.")
            else:
                c1.metric("ESTADO DO HARDWARE", "FALHA CRÍTICA ⚠️")
                c2.metric("CONFIANÇA PREDITIVA", f"{prob_final:.2f}%")
                st.markdown("<style>div[data-testid='stColumn']:nth-child(2) { animation: scada-dark-alert 0.8s infinite alternate !important; } @keyframes scada-dark-alert { 0% { background-color: #11131c; } 100% { background-color: #2d1418; border-color: #dc2626; } }</style>", unsafe_allow_html=True)
                tocar_sirene_militar_ultra()
                
            st.markdown("---")
            if predicao != 0:
                st.markdown("### 🤖 PROTOCOLO CIBER-FÍSICO DE EMERGÊNCIA")
                st.button("⚙️ INICIAR INTERVENÇÃO E MITIGAÇÃO AUTOMÁTICA", on_click=executar_mitigacao_automatica)
                st.markdown("---")
                
            st.subheader("💡 Explicabilidade Estatística (XAI)")
            st.write(f"O algoritmo determinou que o comportamento replica o cenário de **{status}**.")
            
            if st.button("📝 Arquivar Vetor de Anomalia na Base Local"):
                st.session_state.historico_auditoria.append({
                    "Timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
                    "Temp Ar (°C)": air_temp_c, "RPM": rot_speed, "Torque": torque, "Status": status, "Confiança": f"{prob_final:.1f}%"
                })
                st.toast("⚡ Registro inserido na tabela de auditoria!", icon="💾")

    with aba_analytics:
        st.subheader("📊 Validação Métrica do Classificador")
        m1, m2, m3 = st.columns(3)
        m1.metric("Acurácia Geral", f"{acuracia_real:.3f}%")
        m2.metric("Dataset Base", "10.000 Entradas")
        m3.metric("Falsos Negativos", int(matriz_confusao[1][0]))
        fig_scatter = px.scatter(df_original.head(1000), x='Rotational speed [rpm]', y='Torque [Nm]', color='Target', template="plotly_dark")
        st.plotly_chart(fig_scatter, use_container_width=True)

    with aba_explorer:
        st.subheader("🔍 Filtro Avançado do Banco de Dados")
        filtro_tipo = st.selectbox("Selecione a Classe de Maquinário:", df_original['Type'].unique())
        st.dataframe(df_original[df_original['Type'] == filtro_tipo], use_container_width=True)

    with aba_logs:
        st.subheader("📋 Log Oficial de Auditoria do Sistema")
        if st.session_state.historico_auditoria:
            st.dataframe(pd.DataFrame(st.session_state.historico_auditoria), use_container_width=True)
            if st.button("🗑️ Limpar Banco Temporário"):
                st.session_state.historico_auditoria = []
                st.rerun()
        else:
            st.info("Nenhum evento registrado no buffer corrente.")

    with aba_api:
        st.subheader("🌐 Endpoint de Telemetria Industrial (M2M API)")
        st.markdown("Simulação de barramento de dados para integração de sistemas ERP/MES via JSON estruturado.")
        
        payload_telemetria = {
            "gateway_status": "ONLINE",
            "device_uid": "CPS-9981-NX-OL",
            "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
            "sensors": {
                "air_temperature_kelvin": round(st.session_state.sensor_air + 273.15, 2),
                "process_temperature_kelvin": round(st.session_state.sensor_proc + 273.15, 2),
                "rotational_speed_rpm": st.session_state.sensor_rpm,
                "torque_nm": st.session_state.sensor_torque,
                "tool_wear_minutes": st.session_state.sensor_wear
            },
            "ai_inference": {
                "target_class": int(predicao),
                "status_string": status,
                "confidence_score": round(prob_final / 100, 4)
            },
            "security_mesh": {
                "active_mitigation_loop": "READY" if predicao == 0 else "INTERVENTION_REQUIRED",
                "encryption_protocol": "AES-256-GCM"
            }
        }
        
        c_api1, c_api2 = st.columns([2, 1])
        with c_api1:
            st.markdown("### `GET /api/v1/telemetry/live`")
            st.json(payload_telemetria)
        with c_api2:
            st.markdown("### 📡 Conexão do Barramento")
            st.success("🟢 Broker MQTT: Conectado")
            st.info("🔗 Destino: `broker.hivemq.com:1883`")
            st.code("Topic: industrial/cps/shield/metrics", language="bash")
            
            json_string = json.dumps(payload_telemetria, indent=4)
            st.download_button(
                label="📥 Exportar Payload JSON",
                data=json_string,
                file_name=f"telemetry_stream_{int(datetime.datetime.now().timestamp())}.json",
                mime="application/json"
            )

except FileNotFoundError:
    st.error("❌ Erro Crítico: O arquivo 'predictive_maintenance.csv' não foi detectado no repositório.")