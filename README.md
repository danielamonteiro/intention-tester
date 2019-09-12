# intention-tester
Aplicação para automaizar testes de classificação de intenção do Watson Assistant.

### 1. O que é?
Intention tester é uma aplicação simples para ser utilizada na automatização de testes de intenção no Watson Assistant.
Importante para você analisar o desempenho de reconhecimento correto das intenções do seu modelo.

### 2. Só serve para Watson Assistant?
Essa primeira versão sim. Mas a adaptação para outros serviços de classificação de intenção já está em andamento. ;)

### 3. Como usar?
Agora vem a parte legal. A utilização da ferramenta é muito fácil. ;)
1. Faça o clone do projeto na pasta de sua preferência na sua máquina;
2. Lembre-se de fazer a instalação do requirements.txt antes de seguir;
3. Dentro da pasta do projeto, acesse o arquivo service_credentials.json, você vai achá-lo no caminho: app/skills e insira os dados de acesso para o skill do Watson que você deseja testar. Se você tiver mais de um skill, você pode incluí-lo nesse json porque quando você for realizar os testes, você poderá escolher qual skill irá utilizar (não esqueça de salvar o arquivo com as alterações antes de seguir);  
__Dica__: use o campo "name" de uma forma que você consiga fazer a distinção entre os skills que você deseja usar. ;)
4. Agora você deve ir no caminho app/files/teste_files, é nesse caminho que você vai criar os arquivos com as frases que serão testadas. Para isso, é necessário seguir o padrão: o arquivo deve ser de extensão .txt e o nome do arquivo deve ser idêntico ao nome da intenção que você quer testar, ou seja, para cada intenção que você deseja testar, você precisa criar um arquivo diferente, feito isso, você vai preencher esse arquivo com as frases que você deseja testar para essa intenção, cada frase deve estar em uma linha diferente (não esqueça de salvar todos os arquivos antes de seguir);  
**Atenção**: Cada vez que o teste for realizado, ele testará todos os arquivos que estiverem nessa pasta, então sempre verifique os arquivos da pasta antes de iniciar o teste. ;)
5. Vá até a pasta app e execute o arquivo run.py com o comando python3 run.py;
6. Escolha o skill no qual você quer realizar os testes;
7. Insira o nome do arquivo que você quer que seja gerado com o resultado do teste atual - esse arquivo será gerado em formato de .xlsx e estará na pasta app/files/result_files - e verifique se o arquivo foi criado com sucesso, se ele tiver sido criado os testes começarão a ser executados e você será avisado quando todos forem finalizados;
8. Ao receber a mensagem de que os testes foram finalizados, você pode acessar o arquivo com os resultados na pasta indicada acima. :D

