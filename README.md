# APB - IA
    Jorge Luiz Madeira Pires
    Gustavo O. Citadin
    Vitoria dos S. Luiz
    Victor da S. Dagostim
    
🛡️ Cyber-Physical Shield — Sistema Preditivo de Falhas Industriais

> Sistema inteligente de manutenção preditiva com Machine Learning para detecção antecipada de falhas em ativos industriais críticos.

---

## 📋 Sobre o Projeto

O **Cyber-Physical Shield** é um console de monitoramento industrial que utiliza **Inteligência Artificial (Random Forest Classifier)** para prever falhas em equipamentos antes que ocorram. O sistema processa dados de sensores em tempo real — temperatura, rotação, torque e desgaste — e retorna um diagnóstico preditivo com nível de confiança, permitindo intervenção preventiva antes de paradas não planejadas.

**Disciplina:** Inteligência Artificial Aplicada  
**Técnica de IA:** Machine Learning — Random Forest Classifier  
**Interface:** Streamlit (aplicação web interativa)

---

## 🎯 Fluxo do Sistema

```
Entrada de Sensores → Pré-processamento → Random Forest → Diagnóstico + Confiança → Log de Auditoria
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### 1. Clone o repositório (ou extraia o .zip)

```bash
git clone https://github.com/seu-usuario/cyber-physical-shield.git
cd cyber-physical-shield
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> Caso não exista o `requirements.txt`, instale manualmente:

```bash
pip install streamlit pandas scikit-learn plotly
```

### 3. Execute a aplicação

Certifique-se de estar dentro da pasta `app/`:

```bash
cd app
streamlit run aplicativo.py
```
### 3.1 Execute a aplicação

    Se o projeto não executar corretamente, clone o repositório novamente e utilize o arquivo README.md ("Leia-me") para dar continuidade ao processo de inicialização. 

### 4. Acesse no navegador

```
http://localhost:8501
```

---

## 📁 Estrutura do Projeto

```
cyber-physical-shield/
│
└── app/
    ├── aplicativo.py              # Código principal da aplicação Streamlit
    └── predictive_maintenance.csv # Dataset com 10.000 registros industriais
```

---

## 📊 Dataset

| Atributo | Descrição |
|---|---|
| **Fonte** | AI4I 2020 Predictive Maintenance Dataset (UCI / Kaggle) |
| **Registros** | 10.000 entradas |
| **Features usadas** | Temperatura do ar [K], Temperatura do processo [K], Rotação [RPM], Torque [Nm], Desgaste da ferramenta [min] |
| **Variável-alvo** | `Target` — 0 (Normal) / 1 (Falha) |

---

## 🤖 Técnica de IA

**Random Forest Classifier** (Scikit-learn)

| Parâmetro | Valor |
|---|---|
| Estimadores (árvores) | 120 |
| Profundidade máxima | 12 |
| Divisão treino/teste | 80% / 20% |
| Acurácia obtida | ~98% |

O modelo é treinado automaticamente na inicialização da aplicação com cache, garantindo performance mesmo em sessões longas.

---

## 🖥️ Funcionalidades da Interface

| Aba | Descrição |
|---|---|
| 📡 **Telemetria em Tempo Real** | Sliders de sensores, diagnóstico preditivo e protocolo de mitigação automática |
| 📊 **Core Metrics da I.A.** | Acurácia, matriz de confusão e gráfico de dispersão dos dados |
| 🔍 **Data Inventário** | Explorador do dataset com filtro por tipo de maquinário |
| 📋 **Histórico de Logs** | Tabela de auditoria com eventos registrados manualmente |
| 🌐 **Industrial API Gateway** | Simulação de payload JSON para integração ERP/MES (formato M2M) |

---

## ⚠️ Observações

- O arquivo `predictive_maintenance.csv` **deve estar na mesma pasta** que `aplicativo.py`
- A aplicação requer conexão à internet na primeira execução (para carregar fontes do Google Fonts)
- Em caso de falha crítica detectada, um alerta sonoro é ativado automaticamente no navegador

---

## 👥 Integrantes do Grupo

| Nome | Responsabilidade |
|---|---|
| [Nome 1] | Modelagem IA / Random Forest |
| [Nome 2] | Interface Streamlit / Frontend |
| [Nome 3] | Análise de dados / Dataset |
| [Nome 4] | Documentação / Apresentação |
| [Nome 5] | Testes e Validação |

---

## 📄 Licença

Projeto acadêmico desenvolvido para a disciplina de Inteligência Artificial Aplicada.
