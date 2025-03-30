# 💻 Frontend - Vue.js (Vite)

Este diretório contém o frontend da aplicação, desenvolvido com **Vue 3 + Vite**.

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).


---

## ▶️ Como rodar o frontend

### 1. Entrar na pasta `frontend`:
```bash
cd frontend
```

### 2. Instalar as dependências:
```bash
npm install
```

### 3. Rodar o servidor de desenvolvimento:
```bash
npm run dev
```

> O projeto será iniciado em: [http://localhost:5173](http://localhost:5173)

---

## 📂 Estrutura

- `src/App.vue` → Componente principal com interface de busca
- `main.js` → Inicialização da aplicação
- `style.css` → Estilos globais (se usados)
- `vite.config.js` → Configurações do Vite

---

## 🔗 Integração com o Backend

O frontend está configurado para fazer requisições para:

```
http://localhost:8000/buscar
```

Caso o backend rode em outra porta ou domínio, altere o endpoint no `App.vue`.

---

## 🎯 Funcionalidade

Permite buscar operadoras de saúde por:

- Razão Social
- Nome Fantasia
- CNPJ
- Cidade
- UF
- Representante

Os resultados são exibidos em uma tabela estilizada.

---

## 📌 Observações

- Use o backend ativo antes de iniciar o frontend para que as requisições funcionem corretamente.