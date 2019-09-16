import csv
import math
import operator

## Carrega os exemplos de treinamento da forma (atrioutos_nao_alvo, atributo_alvo)
def loadDataset(filename):
    dataMatrix = []
    dataLabels = []
    with open(filename) as file:
        rows = csv.reader(file, delimiter=',')
        for row in rows:
            vector = []
            for i in range(0, len(row)-1):
                vector.append(float(row[i]))
            dataMatrix.append(vector)
            dataLabels.append(float(row[len(row)-1]))
    return (dataMatrix, dataLabels)

## Calcula a distancia euclidiana entre dois exemplos
def euclideanDistance(sampleX, sampleY):
    euclideanDistance = 0.0
    for i in range(len(sampleX)):
        euclideanDistance += (sampleX[i] - sampleY[i]) ** 2
    euclideanDistance = math.sqrt(euclideanDistance)
    return euclideanDistance

## Query => Entrada a ser classificada
## K => Quantidade de grupos
## Filename => Nome da base de dados que contem os exemplos (Formato csv)
## Weighted => Knn é ponderado ou não (Por padrão não)
def classify(query, k=3, filename='database.csv', weighted=False):
    nearestNeighbor = []
    (dataMatrix, dataLabels) = loadDataset(filename)

    ## Calcula os K vizinhos mais proximos
    for i in range(len(dataMatrix)):
        distance = euclideanDistance(query, dataMatrix[i])
        
        if weighted and distance != 0.0:
            distance = 1 / math.pow(distance, 2)

        if len(nearestNeighbor) > k:
            for j in range(len(nearestNeighbor)):
                ( _, distanceSample ) = nearestNeighbor[j]
                if ( distance < distanceSample ):
                    nearestNeighbor[j] = (i, distance)
        else:
            nearestNeighbor.append((i, distance))
    
    ## Calcula a ocorrencia de cada um dos valores do atributo alvo nos k vizinhos mais proximos
    occurrences = dict()
    for (i, _ )  in nearestNeighbor:
        label = str(dataLabels[i])
        occurrences[label] = occurrences.get(label, 0) + 1

    ## Seleciona o valor com maior ocorrencia 
    return max(occurrences.items(), key=operator.itemgetter(1))[0]

def main():
    query = [6.0, 3.4, 4.5, 1.6]
    print('Query: ' + str(query))
    print('Class: ' + classify(query, k=3, filename='iris.csv'))

if __name__ == "__main__":
    main()