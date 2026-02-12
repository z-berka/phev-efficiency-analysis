import matplotlib.pyplot as plt

def plot_energy_vs_speed(df):
    plt.figure()
    plt.scatter(df["Mean Velocity [km/h]"], df["Total Energy [Wh/km]"])
    plt.xlabel("Mean Speed [km/h]")
    plt.ylabel("Total Energy [Wh/km]")
    plt.title("Energy Consumption vs Speed")
    plt.show()

def plot_urban_share_effect(df):
    plt.figure()
    plt.scatter(df["Urban Share"], df["Total Energy [Wh/km]"])
    plt.xlabel("Urban Share")
    plt.ylabel("Total Energy [Wh/km]")
    plt.title("Urban Driving Impact on Energy Consumption")
    plt.show()
