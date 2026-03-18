[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_c4XDR90)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23169854)
# PRÁTICA AVALIADA 1 - ES1 (10 pontos)

**Módulo/Semana:** 4  
**Conteúdo avaliado:** Módulos 1, 2 e 3 (Unidades 1, 2 e 3)  
**Duração sugerida:** 2 horas  
**Tipo:** Prática integradora avaliativa

---

## CONTEXTUALIZAÇÃO

Uma startup de tecnologia chamada **"AgileTech Solutions"** está iniciando o desenvolvimento de um novo sistema web para gestão de projetos ágeis. A empresa decidiu adotar práticas ágeis desde o início e precisa estruturar adequadamente seu processo de desenvolvimento.

Você foi contratado como **Engenheiro de Software** para:
1. Analisar a situação atual da empresa e propor melhorias baseadas em princípios ágeis
2. Estruturar um processo de desenvolvimento utilizando XP e Scrum
3. Aplicar o conceito de Design Simples em um cenário prático de código

---

## QUESTÃO 1: Análise de Processo e Manifesto Ágil (3,5 pontos)

### Contexto

A AgileTech Solutions possui os seguintes desafios:
- Equipe pequena (5 desenvolvedores, 1 product owner)
- Cliente participativo mas com disponibilidade limitada
- Requisitos iniciais vagos e sujeitos a mudanças frequentes
- Pressão por entregas rápidas para demonstrar valor ao mercado
- Histórico de projetos anteriores com documentação extensa que rapidamente ficava desatualizada

### Enunciado

**a) (1,5 pontos)** Elabore um documento markdown (`analise-processo.md`) explicando:
- Como os **4 valores** do Manifesto Ágil se aplicam ao contexto da AgileTech
- Justifique a escolha de uma abordagem ágil ao invés de um processo tradicional (cascata) para este cenário
- Identifique pelo menos **3 práticas ágeis** que a empresa deveria adotar imediatamente

**b) (1,0 ponto)** No mesmo arquivo `analise-processo.md`, inclua uma seção sobre **Programação em Pares**:
- Explique o conceito de pair programming e seus benefícios
- Discuta os **desafios** de aplicar programação em pares em um curso à distância
- Proponha **2 alternativas ou adaptações** dessa prática que seriam viáveis para equipes remotas (como no contexto deste curso EAD)

**c) (1,0 ponto)** Considerando os desafios da empresa, identifique no arquivo `analise-processo.md`:
- Quais das **dificuldades essenciais** de Brooks (complexidade, conformidade, mutabilidade, invisibilidade) são mais relevantes neste contexto?
- Como a adoção de métodos ágeis pode ajudar a mitigar essas dificuldades?

### Critérios de Avaliação

| Critério | Pontuação |
|----------|-----------|
| Aplicação correta dos 4 valores do Manifesto Ágil ao contexto | 0,7 |
| Justificativa clara e fundamentada da escolha ágil vs cascata | 0,5 |
| Identificação e explicação de 3 práticas ágeis relevantes | 0,3 |
| Explicação de pair programming e benefícios | 0,3 |
| Discussão dos desafios em EAD | 0,3 |
| Propostas de adaptação para equipes remotas | 0,4 |
| Análise das dificuldades essenciais de Brooks | 0,6 |
| Proposta de mitigação através de métodos ágeis | 0,4 |

---

## QUESTÃO 2: Estruturação de Processo XP e Scrum (3,5 pontos)

### Contexto

A equipe decidiu combinar práticas de **Extreme Programming (XP)** e **Scrum** para estruturar seu processo de desenvolvimento.

### Enunciado

**a) (2,0 pontos)** Crie um quadro Kanban no **GitHub Projects** que represente o fluxo de trabalho da equipe, incorporando elementos tanto de XP quanto de Scrum:
- Configure as colunas apropriadas
- Adicione pelo menos 5 cards representando user stories ou tarefas
- No arquivo `processo-xp-scrum.md`, documente:
  - As **práticas de XP** que serão adotadas pela equipe (escolha no mínimo 5)
  - Como essas práticas se integram ao framework Scrum
  - O fluxo de trabalho semanal da equipe (planning, daily, review, retrospectiva)
  - **Link para o quadro GitHub Projects criado**

**b) (1,5 pontos)** **No mesmo arquivo `processo-xp-scrum.md`**, elabore:
- Um cronograma de uma **Sprint** de 2 semanas, detalhando:
  - Cerimônias do Scrum (quando ocorrem, duração, participantes)
  - Momentos de aplicação das práticas de XP ao longo da Sprint
  - Entregas esperadas ao final da Sprint
- Uma tabela comparando Scrum e Kanban, destacando:
  - Quando usar cada um
  - Principais diferenças
  - Como podem ser combinados

### Critérios de Avaliação

| Critério | Pontuação |
|----------|-----------|
| Quadro Kanban bem estruturado com user stories | 0,6 |
| Identificação e explicação de 5 práticas XP | 0,7 |
| Integração coerente entre XP e Scrum | 0,4 |
| Detalhamento do fluxo de trabalho semanal | 0,3 |
| Cronograma de Sprint completo e realista | 0,8 |
| Tabela comparativa Scrum vs Kanban fundamentada | 0,7 |

---

## QUESTÃO 3: Design Simples - Princípio YAGNI (3,0 pontos)

### Contexto

Um desenvolvedor júnior da AgileTech criou uma classe Python para gerenciar usuários do sistema. Ele tentou antecipar todas as possíveis necessidades futuras, mas acabou violando o princípio **YAGNI (You Aren't Gonna Need It)** - um dos pilares do **Design Simples** em XP.

Atualmente, o sistema precisa apenas:
- Cadastrar usuários com nome, email e senha
- Fazer login validando email e senha
- Listar todos os usuários

### Código Atual (Viola YAGNI)

O código atual está disponível no arquivo [src/usuario_simples.py](src/usuario_simples.py).

Analise o código e observe as duas classes:
- **`Usuario`**: contém diversos atributos e métodos além dos requisitos atuais
- **`GerenciadorUsuarios`**: implementa muitas funcionalidades extras

### Enunciado

**a) (1,0 ponto)** No arquivo `analise-yagni.md`, identifique e liste:
- Todos os atributos da classe `Usuario` que **não são necessários** no momento
- Todos os métodos que **não são necessários** no momento
- Explique brevemente **por que** cada item listado viola o princípio YAGNI

**b) (2,0 pontos)** No arquivo `src/usuario_simples.py`, refatore o código existente para uma versão **simplificada** que:
- Mantém **apenas** as funcionalidades realmente necessárias
- Remove toda complexidade desnecessária
- Continua funcional para os requisitos atuais (cadastrar, fazer login, listar)

O código simplificado deve incluir:
- Classe `Usuario` com apenas atributos necessários
- Classe `GerenciadorUsuarios` com apenas métodos necessários
- Validação de senha (hash pode ser mantido pois é segurança básica)
- Validação de email duplicado

### Estrutura de Arquivos Esperada

```
es1-pratica-avaliada-1/
├── .gitignore
├── README.md
├── analise-processo.md
├── processo-xp-scrum.md
├── analise-yagni.md
└── src/
    └── usuario_simples.py
```

### Critérios de Avaliação

| Critério | Pontuação |
|----------|-----------|
| Identificação completa de atributos desnecessários | 0,3 |
| Identificação completa de métodos desnecessários | 0,3 |
| Explicação adequada das violações de YAGNI | 0,4 |
| Código simplificado mantém funcionalidades necessárias | 0,6 |
| Remoção efetiva de complexidade desnecessária | 0,6 |
| Código limpo e bem organizado | 0,3 |
| Validações essenciais mantidas | 0,5 |

---

## MATERIAL DIDÁTICO

Conforme Plano de Estudos das Unidades 1, 2 e 3.

---

## ENTREGA

1. **Repositório GitHub** contendo todos os arquivos da prática
2. **Link do repositório** deve ser submetido na plataforma de ensino
3. **GitHub Projects** configurado e vinculado ao repositório
4. **Documentação clara** em todos os arquivos markdown

### Prazos
- **Início:** Módulo/Semana 4
- **Entrega:** Final do Módulo/Semana 4
- **Feedback:** Módulo/Semana 5

---

## IMPORTANTE

- Esta é uma **avaliação individual**
- Consulta aos materiais didáticos é **permitida e encorajada**
- Plágio será **penalizado com nota zero**
- Dúvidas devem ser encaminhadas ao tutor através dos canais oficiais
- A prática simula situações reais de trabalho em engenharia de software
- O código simplificado **não precisa ter testes** - foque na simplicidade

---

## OBSERVAÇÕES SOBRE CORREÇÃO

- A correção será feita através de análise manual dos documentos markdown
- O código Python será validado através de **testes automatizados do professor**
- Os testes automatizados verificarão se as funcionalidades básicas (cadastrar, login, listar) continuam funcionando
- Você **não precisa criar testes** - apenas garantir que seu código simplificado funcione
