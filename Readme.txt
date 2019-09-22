Fonte:
    http://archive.ics.uci.edu/ml/datasets/Parkinsons+Telemonitoring

Descrição
    O conjunto de dados foi criado por Athanasios Tsanas (tsanasthanasis '@' gmail.com) e Max Little (littlem '@' physics.ox.ac.uk) da Universidade de Oxford, 
em colaboração com 10 centros médicos nos EUA e na Intel Corporation que desenvolveu o dispositivo de telemonitoramento para gravar os sinais de fala.
O estudo original usou uma gama de métodos de regressão linear e não linear para prever o escore de sintomas da doença de Parkinson do clínico na escala UPDRS.
Este conjunto de dados é composto por uma série de medições biomédicas de voz de 42 pessoas com doença de Parkinson em estágio inicial 
recrutadas para um teste de seis meses de um dispositivo de telemonitoramento para monitoramento remoto da progressão dos sintomas.

Informações sobre atributos:
    indivíduo - Número inteiro que identifica exclusivamente cada indivíduo
    idade - Idade do indivíduo
    sexo - Sexo do indivíduo '0' - masculino, '1' - feminino
    test_time - Tempo desde o recrutamento para o julgamento. A parte inteira é o número de dias desde o recrutamento.
    motor_UPDRS - Pontuação UPDRS motora do clínico, total interpolado linearmente_UPDRS - Pontuação UPDRS total do clínico, interpolada linearmente
    Tremulação (%), Tremulação (Abs), Tremulação: RAP, Tremulação: PPQ5, Tremulação: DDP - Diversas medidas de variação na frequência fundamental
    Shimmer, Shimmer (dB), Shimmer: APQ3, Shimmer: APQ5, Shimmer: APQ11, Shimmer: DDA - Várias medidas de variação de amplitude
    NHR, HNR - Duas medidas de razão de ruído para componentes tonais na voz
    RPDE - Uma medida de complexidade dinâmica não linear
    DFA - Expoente de escala fractal de sinais
    EPI - Uma medida não-linear da variação de frequência fundamental

Arquivos csv :
    parkinsons_updrs.csv - base de dados utilizado para aprendizagem
    queries.csv - entrada de exemplos para serem classificados

Execucão
    python knn.py k
    k = tamanho do agrupamento para o algoritmo knn

Saída:
    Toda saida é gerada em no console, no seguinte formato
    Entrada => Classificao