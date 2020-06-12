## PROJETO DE CES 22

Alunos: Caio Graça Gomes e José Victor Marques dos Reis Melo

Projeto de jogo estilo Air-Hockey, foi utilizada uma arquitetura Observer para a implementação, dissociando o back e o front elementos básicos do jogo a partir de um gerenciador de eventos.

Em config encontram-se constantes fundamentais do jogo que podem ser facilmente alteradas, como a velocidade de referência do disco, do controlador, tamanho do gol, etc.

Em model encontram-se as implementações das unidades elementares do jogo, tais quais o disco e o placar, todas as configurações dos elementos básicos do jogo em um dado instante unidas são o que definem o estado do jogo, e, a depender do estado, o gerenciador de eventos pode postar um evento que altere o front do jogo

Em subscriber encontra-se a implementação do gerenciador de eventos e dos eventos em si, esses eventos podem ser inicialização término, gol, evento padrão (nada de relevante ocorreu), etc.

Em view encontra-se a implementação do front end de todas as unidades básicas do jogo, que podem ser atualizados por intérmedio do gerenciador de eventos

A main apenas precisa rodar a game_engine que se encontra em game/model/game.py

Para jogar basta fazer "python3 main.py" na prompt de comando. Os comandos internos do jogo como continuar, resetar e quitar são acionados pelo mouse