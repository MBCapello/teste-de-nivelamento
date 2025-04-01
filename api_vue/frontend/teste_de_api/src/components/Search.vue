<template>
    <div class="search-container">
      <h2>Buscar Operadoras</h2>
  
      <!-- Input de Pesquisa -->
      <input 
        type="text" 
        v-model="query" 
        @input="onSearch" 
        placeholder="Digite o nome fantasia" 
      />
  
      <!-- Indicador de Carregamento -->
      <div v-if="loading">Carregando...</div>
  
      <!-- Exibir Resultados -->
      <div v-if="results.length > 0">
        <ul>
          <li v-for="item in results" :key="item.cnpj">
            <p><h4>Nome: </h4><strong>{{ item.nome_fantasia }}</strong></p>
            <p><h4>Razão social: </h4>{{ item.razao_social }}</p>
            <p><h4>CNPJ: </h4>{{ item.cnpj }}</p>
            <p><H4>Telefone: </H4>({{ item.ddd }}) {{ item.telefone }}</p>
          </li>
        </ul>
      </div>
  
      <!-- Mensagem de Erro -->
      <div v-if="error" class="error-message">
        <p>{{ error }}</p>
      </div>
  
      <!-- Mensagem se não houver resultados -->
      <div v-if="results.length === 0 && !loading && query">
        <p>Nenhum resultado encontrado</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        query: "", // Termo de pesquisa
        results: [], // Resultados da pesquisa
        loading: false, // Estado de carregamento
        error: null, // Erro da API
      };
    },
    methods: {
      // Função que chama a API para buscar dados
      onSearch() {
        if (this.query.trim() === "") {
          this.results = []; // Limpar resultados se a consulta for vazia
          return;
        }
  
        this.loading = true;
        this.error = null; // Limpar erros anteriores
  
        // Fazer a requisição GET para a API Flask
        axios
  .get(`http://127.0.0.1:5000/search`, {
    params: { query: this.query },
  })
  .then((response) => {
    console.log("🔍 API Response:", response.data); // Verifica o retorno do backend
    this.results = response.data;
    console.log("📊 Vue Results:", this.results); // Verifica se o Vue está armazenando os dados corretamente
  })
  .catch((err) => {
    this.error = "Ocorreu um erro ao buscar os dados.";
    console.error("❌ Erro na requisição:", err);
  })
  .finally(() => {
    this.loading = false;
  });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos para o componente de busca */
  .search-container {
    margin: 20px;
  }
  
  input[type="text"] {
    padding: 10px;
    font-size: 16px;
    width: 100%;
    max-width: 400px;
    margin-bottom: 20px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 15px;
  }
  
  .error-message {
    color: red;
  }
  </style>
  