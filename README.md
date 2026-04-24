#  Chatbot Técnico - Nobreak NXR 15–90kVA

Projeto desenvolvido para a empresa **Luffy Chat Bots Ltda.**, com o objetivo de criar um chatbot inteligente de suporte técnico para o nobreak **NXR 15–90kVA**.

---

##  Objetivo

Desenvolver um sistema que auxilie usuários a:

* Diagnosticar alarmes do nobreak
* Entender mensagens do sistema
* Consultar soluções diretamente do manual técnico
* Reduzir a carga de trabalho da equipe de suporte

---

##  Tecnologias Utilizadas

* Python
* Streamlit (interface web interativa)
* LangChain (orquestração de IA)
* OpenAI API (modelo de linguagem)
* Pandas (manipulação de dados)
* CSV (base estruturada de alarmes)

---

##  Funcionamento

O sistema utiliza um modelo de IA integrado com uma base de dados estruturada (`alarmes.csv`) extraída do manual técnico do equipamento.

###  Fluxo:

1. Usuário realiza autenticação (OBJETO ESPECÍFICO)
2. Sistema valida acesso
3. LED virtual é ativado (simulação)
4. Usuário faz uma pergunta
5. O sistema:

   * Busca informações relevantes no CSV (RAG simples)
   * Envia contexto + pergunta para a IA
6. IA responde com base no manual

---

##  Sistema de Segurança

O acesso ao chatbot é restrito:

* Apenas usuários com código autorizado podem utilizar
* Simula o conceito de “OBJETO ESPECÍFICO”
* Ao autenticar:

  *  Acesso liberado
  *  LED virtual é ativado

---

##  Base de Dados

Arquivo: `alarmes.csv`

Contém:

* Nome do alarme
* Descrição
* Solução recomendada

Baseado diretamente no:

* Capítulo 5.5 – Alarm List
* Manual do Nobreak NXR

---

## 💬 Exemplo de Uso

**Usuário:**

> "Battery Low Pre-warning"

**Resposta do sistema:**

> A bateria está próxima da descarga completa. Desligue a carga antes da descarga total.

---


##  Estrutura do Projeto

```
/projeto
 ├── app.py
 ├── alarmes.csv
 ├── README.md
```

---

##  Melhorias Futuras

* Implementação de embeddings (RAG avançado)
* Upload de PDF automático
* Interface mais avançada
* Integração com banco de dados
* Autenticação real (RFID / QR Code)
* Deploy em nuvem

---

## Conclusão

Este projeto entrega uma solução funcional e escalável para suporte técnico automatizado, utilizando inteligência artificial e dados estruturados para fornecer respostas precisas e confiáveis.

---

##  Autor

Desenvolvido por [Vinicius Pini]

---
