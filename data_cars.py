"""coding: utf-8"""
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def extract_data():

    index = {'SIMSEC': 0,
             'NO': 1,
             'LANE/LINK/NO': 2,
             'LANE/INDEX': 3,
             'POS': 4,
             'POSLAT': 5,
             'ACCELERATION': 6,
             'VEHTYPE': 7,
             'SPEED': 8,
             'TMINNETTOT': 9,
             'COORDFRONTX': 10,
             'DISTTRAVTOT': 11}

    dados_brutos = pd.read_fwf('/home/jeferson/PycharmProjects/Kaggle_Challenges/gil/CARRO_001.fzp', header=None)
    dados_brutos = dados_brutos[0][25:]

    dados_limpos = []

    for it in dados_brutos:
        var = it.split(';')
        dados_limpos.append(var)

    dados_tratados = np.zeros(len(dados_limpos[0]) * len(dados_limpos)).reshape(len(dados_limpos), len(dados_limpos[0]))

    i = 0
    while i < len(dados_limpos):
        j = 0
        while j < len(dados_limpos[0]):
            dados_tratados[i][j] = float(dados_limpos[i][j])
            j = j + 1
        i = i + 1

    dados_tratados = dados_tratados.transpose()

    return np.array([dados_tratados[index['NO']],
                     dados_tratados[index['SPEED']],
                     dados_tratados[index['ACCELERATION']],
                     dados_tratados[index['TMINNETTOT']]
                     ]).transpose()


def plot_graph(data, n_car):
    data_car = []
    for it in data:
        if it[0] == n_car:
            data_car.append(it)

    data_car = np.array(data_car)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.scatter(xs=data_car.T[1], ys=data_car.T[2], zs=data_car.T[3], zdir='z', s=20, c=None,
               depthshade=True, marker='.')
    ax.set_xlabel('VELOCIDADE')
    ax.set_ylabel('ACELERAÇÃO')
    ax.set_zlabel('TEMPO')
    ax.set_title('VELOCIDADE, ACELERAÇÃO E TEMPO DO CARRO ' + str(n_car))
    ax.grid(False)
    plt.show()


if __name__ == '__main__':

    dados = extract_data()

    while True:
        print('Para encerrar, digite "exit"')
        car = (input("Digite o código de um veiculo :"))
        if car == 'exit':
            exit()
        plot_graph(dados, car)
