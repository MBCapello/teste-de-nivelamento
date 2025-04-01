-- Usa o banco de dados ans_operadoras
USE ans_operadoras;

-- Dropar as tabelas caso existam para garantir que estamos criando do zero
DROP TABLE IF EXISTS operadoras;
DROP TABLE IF EXISTS demonstracoes_contabeis;

-- Criação da tabela operadoras
CREATE TABLE IF NOT EXISTS operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único
    Registro_ANS VARCHAR(100) NOT NULL UNIQUE, -- Registro único da ANS
    CNPJ VARCHAR(100), -- CNPJ da operadora
    Razao_Social VARCHAR(255), -- Razão social
    Nome_Fantasia VARCHAR(255), -- Nome fantasia
    Modalidade VARCHAR(100), -- Modalidade (ex: Saúde Suplementar)
    Logradouro VARCHAR(255), -- Endereço
    Numero VARCHAR(50), -- Número do endereço
    Complemento VARCHAR(100), -- Complemento do endereço
    Bairro VARCHAR(100), -- Bairro
    Cidade VARCHAR(100), -- Cidade
    UF CHAR(2), -- Unidade Federativa (Estado)
    CEP VARCHAR(10), -- Código postal
    DDD VARCHAR(3), -- Código DDD do telefone
    Telefone VARCHAR(20), -- Telefone da operadora
    Fax VARCHAR(20), -- Fax (se disponível)
    Endereco_eletronico VARCHAR(255), -- Endereço de e-mail ou site
    Representante VARCHAR(255), -- Nome do representante
    Cargo_Representante VARCHAR(100), -- Cargo do representante
    Regiao_de_Comercializacao VARCHAR(255), -- Região de atuação
    Data_Registro_ANS DATE -- Data de registro na ANS
);

-- Criação da tabela demonstracoes_contabeis
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único
    DATA DATE NOT NULL, -- Data do demonstrativo contábil
    REG_ANS VARCHAR(100) NOT NULL, -- Registro da ANS da operadora
    CD_CONTA_CONTABIL VARCHAR(100), -- Código da conta contábil (se necessário)
    DESCRICAO TEXT, -- Descrição das despesas
    VL_SALDO_INICIAL DECIMAL(15,2), -- Saldo inicial
    VL_SALDO_FINAL DECIMAL(15,2) -- Saldo final
);