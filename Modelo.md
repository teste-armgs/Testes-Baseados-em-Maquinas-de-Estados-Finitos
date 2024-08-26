---
marp: true
theme: default
class: 
  - lead
backgroundImage: url('./../if_back1.png')

paginate: true
---
 
# Testes com Integração Contínua (CI) e Desenvolvimento Contínuo (CD) 
### Prof. Dr. Valério Gutemberg
#### :pencil: Aluno: Moisés, Aluno Rafael Algusto, Aluno Alexandro, Aluno Gruilherme Cadete
#### :pencil: Disciplina de Testes de Software
:pencil2: Curso de Sistemas para Internet


---
## O que é CI e CD?

- **Integração Contínua (CI)**: Prática de integrar código frequentemente e automatizar testes para garantir que o software funcione corretamente.
- **Desenvolvimento Contínuo (CD)**: Extensão do CI, automatizando a entrega de software em ambientes de produção de maneira rápida e segura.





---

## Benefícios do CI/CD

- **Detecção rápida de erros**: Testes automáticos após cada integração.
- **Automação de deploy**: Minimiza erros manuais.
- **Feedback contínuo**: Progresso rápido no desenvolvimento.
- **Redução de tempo de entrega**: Acelera a entrega de novas funcionalidades e correções.

---
## Tecnologias de CI/CD

### Jenkins
- Plataforma open-source para automação de processos.
- Amplamente usada para CI/CD.
- Suporta integração com várias ferramentas de teste.

### GitHub Actions
- Integra CI/CD diretamente no repositório do GitHub.
- Suporte nativo a PyTest, Go Test e Rust Test.
- Configuração simplificada com workflows YAML.





---

### Travis CI
- Serviço baseado na nuvem para CI/CD.
- Suporte a múltiplas linguagens de programação.
- Integração fácil com repositórios GitHub.

---
## Ferramentas de Teste

### PyTest (Python)
- Framework de testes para Python.
- Suporte a testes unitários e de integração.
- Integração fácil com Jenkins, GitHub Actions e Travis CI.

### Go Test (Go)
- Ferramenta nativa de testes para Go.
- Executa testes unitários, benchmarks e de integração.
- Totalmente suportado nas pipelines CI/CD.



---

### Rust Test (Rust)
- Framework nativo para testar aplicações Rust.
- Fácil integração em pipelines de CI/CD.
- Verifica segurança, desempenho e consistência do código.


---

## Exemplo de Pipeline CI/CD (GitHub Actions)
```yaml
name: CI Pipeline
on:
  push:
    branches:
      - main
      
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Configurar Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - name: Instalar Dependências
        run: pip install pytest
      - name: Executar Testes
        run: pytest
```
---

## Conclusão
    O CI/CD automatiza e acelera o processo de desenvolvimento.
A combinação com ferramentas de teste garante a qualidade do software.
Integração eficiente entre Jenkins, GitHub Actions e Travis CI com PyTest, Go Test e Rust Test


---



# Obrigado!

Dúvidas?

