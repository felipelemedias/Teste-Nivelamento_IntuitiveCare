<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>

    <div class="input-group">
      <select v-model="campo">
        <option disabled value="">Escolha o campo</option>
        <option value="Razao_Social">Razão Social</option>
        <option value="CNPJ">CNPJ</option>
        <option value="Nome_Fantasia">Nome Fantasia</option>
        <option value="Cidade">Cidade</option>
        <option value="UF">UF</option>
        <option value="Representante">Representante</option>
      </select>

      <input v-model="termo" type="text" placeholder="Digite o termo..." />
      <button @click="buscarOperadoras">Buscar</button>
    </div>

    <div v-if="resultado.length" class="result-container">
      <h2>Resultados:</h2>
      <table class="result-table">
        <thead>
          <tr>
            <th>Razão Social</th>
            <th>CNPJ</th>
            <th>Modalidade</th>
            <th>Endereço</th>
            <th>Cidade/UF</th>
            <th>Telefone</th>
            <th>Email</th>
            <th>Representante</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(operadora, index) in resultado" :key="index">
            <td>{{ operadora.Razao_Social }}</td>
            <td>{{ operadora.CNPJ }}</td>
            <td>{{ operadora.Modalidade }}</td>
            <td>{{ operadora.Logradouro }} {{ operadora.Numero }} - {{ operadora.Bairro }}</td>
            <td>{{ operadora.Cidade }}/{{ operadora.UF }}</td>
            <td>({{ operadora.DDD }}) {{ operadora.Telefone }}</td>
            <td>{{ operadora.Endereco_eletronico }}</td>
            <td>{{ operadora.Representante }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-if="erro" class="erro">{{ erro }}</p>
  </div>
</template>


<script>
import { ref } from 'vue'

export default {
  setup() {
    const campo = ref("")
    const termo = ref("")
    const resultado = ref([])
    const erro = ref("")

    const buscarOperadoras = async () => {
  erro.value = ""
  resultado.value = []

  if (!campo.value || !termo.value) {
    erro.value = "Selecione um campo e digite um termo para buscar."
    return
  }

  try {
    const url = `http://localhost:8000/buscar?campo=${encodeURIComponent(campo.value)}&termo=${encodeURIComponent(termo.value)}`
    const response = await fetch(url)
    if (!response.ok) throw new Error("Erro na requisição")

    const data = await response.json()

    if (Array.isArray(data) && data.length === 0) {
      erro.value = "Nenhum resultado encontrado para sua busca."
    } else {
      resultado.value = data
    }
  } catch (err) {
    erro.value = "Erro ao buscar operadoras."
  }
}

    return { campo, termo, resultado, erro, buscarOperadoras }
  }
}
</script>



<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

.input-group {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.result-container {
  margin-top: 20px;
}

.result-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.result-table th,
.result-table td {
  border: 1px solid #ddd;
  padding: 8px;
}

.result-table th {
  background-color: #0056b3;
  font-weight: bold;
}

.erro {
  color: red;
  margin-top: 20px;
}  

</style>
