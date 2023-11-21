import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 12]

    fig, ax = plt.subplots()   #fig: figura ax: coordenadas en las que vamos a graficar
    ax.pie(values, labels=labels)    #genero grafica de pie
    # ax.axis("equal")
    plt.savefig("pie.png")
    plt.close()
