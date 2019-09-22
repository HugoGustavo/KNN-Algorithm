import csv
import sys
import math
import operator

## Carrega os exemplos de treinamento da forma (atributos_nao_alvo, atributo_alvo)
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

## Carrega os exemplos a serem classificados
def loadQueries(filename):
    dataMatrix = []
    with open(filename) as file:
        rows = csv.reader(file, delimiter=',')
        for row in rows:
            vector = []
            for i in range(0, len(row)):
                vector.append(float(row[i]))
            dataMatrix.append(vector)
    return dataMatrix

## Calcula a distancia euclidiana entre dois exemplos
def euclideanDistance(sampleX, sampleY):
    euclideanDistance = 0.0
    for i in range(len(sampleX)):
        euclideanDistance += (sampleX[i] - sampleY[i]) ** 2
    euclideanDistance = math.sqrt(euclideanDistance)
    return euclideanDistance

def knn(k, dataMatrix, dataLabels, query):
    nearestNeighbor = []

    ## Calcula os K vizinhos mais proximos
    for i in range(len(dataMatrix)):
        distance = euclideanDistance(query, dataMatrix[i])

        if len(nearestNeighbor) > k:
            for j in range(len(nearestNeighbor)):
                ( _, distanceSample ) = nearestNeighbor[j]
                if ( distance < distanceSample ):
                    nearestNeighbor[j] = (i, distance)
        else:
            nearestNeighbor.append((i, distance))
    
    ## Calcula a media dos valores do atributo alvo nos k vizinhos mais proximos
    sum = 0.0
    for (i, _ )  in nearestNeighbor:
        sum = sum + float(dataLabels[i])
    target = sum / float(k)
    
    return target

def classify(k=3):
    (dataMatrix, dataLabels) = loadDataset('parkinsons_updrs.csv')
    queries = loadQueries('queries.csv')

    for query in queries:
        target = knn(k, dataMatrix, dataLabels, query)
        print(str(query) + ' => ' + str(target))

def main():
    k = int(sys.argv[1])
    classify(k)

if __name__ == "__main__":
    main()