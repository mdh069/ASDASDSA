const fs = require("fs")
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const createFile = (nameFile, extensionFile, contentFile) => {
    fs.writeFile(`${__dirname}/${nameFile}.${extensionFile}`, contentFile, () => {
        console.log("Arquivo Criado")
    })
}

const navegar_diretorio = async () => {
    while(true){
        console.log(`Voçê esta em ${__dirname}`)
        console.log("Digite o numero da sua ação: ")
        const acao = rl.question("\n1 - Criar arquivo \n2 - Excluir arquivo \n3 - Ler arquivo", (data) => data)
        break
    }
}

navegar_diretorio()