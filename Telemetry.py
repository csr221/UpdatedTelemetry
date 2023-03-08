import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd
ff1.Cache.enable_cache('cache')
year, grand_prix, session = 2023, "Testing", "Q"
testingSession = ff1.get_testing_session(2023,1,2)
testingSession.load()
driver_1 = "ALO"
driver_2 = "PER"
driver_3 = "VER"
session_driver_1 = testingSession.laps.pick_driver(driver_1)
session_driver_2 = testingSession.laps.pick_driver(driver_2)
session_driver_3 = testingSession.laps.pick_driver(driver_3)
driver_1_fastest = session_driver_1.pick_fastest()
driver_2_fastest = session_driver_2.pick_fastest()
driver_3_fastest = session_driver_3.pick_fastest()

team_driver_1 = driver_1_fastest['Team']
team_driver_2 = driver_2_fastest['Team']
team_driver_3 = driver_3_fastest['Team']

telemetry_driver_1 = driver_1_fastest.get_telemetry().add_distance()
telemetry_driver_2 = driver_2_fastest.get_telemetry().add_distance()
telemetry_driver_3 = driver_3_fastest.get_telemetry().add_distance()

delta_time, ref_tel,compare_tel = utils.delta_time(driver_1_fastest, driver_2_fastest)
delta_time2, ref_tel2,compare_tel2 = utils.delta_time(driver_3_fastest, driver_2_fastest)
plot_size = [15,15]
plot_title = f"{testingSession.event.year} {testingSession.event.EventName} - {testingSession.name} - {driver_1} VS {driver_2} VS {driver_3}"

plot_ratios = [100]
plot_filename = "TestingRPMBestLap.pdf"
plt.xscale = 100
plt.rcParams['figure.figsize'] = plot_size

fig, ax = plt.subplots(1, gridspec_kw={'height_ratios': plot_ratios})

"""
ax[0].title.set_text(plot_title)

# Delta line

ax[0].axhline(0)
ax[0].set(ylabel=f"Gap to {driver_2} (s)")
ax[0].plot(ref_tel2['Distance'], delta_time2)
ax[0].axhline(0)
ax[0].set(ylabel=f"Gap to {driver_2} (s)")

# Speed trace
ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1,
           color=ff1.plotting.team_color(team_driver_1))
ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2,
           color=ff1.plotting.team_color(team_driver_2))
ax[1].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Speed'], label=driver_3,
           color=ff1.plotting.team_color(team_driver_3))
ax[1].set(ylabel='Speed')
ax[1].legend(loc="lower right")

# Throttle trace
ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1,
           color=ff1.plotting.team_color(team_driver_1))
ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2,
           color=ff1.plotting.team_color(team_driver_2))
ax[2].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Throttle'], label=driver_3,
           color=ff1.plotting.team_color(team_driver_3))
ax[2].set(ylabel='Throttle')

# Brake trace
ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1,
           color=ff1.plotting.team_color(team_driver_1))
ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2,
           color=ff1.plotting.team_color(team_driver_2))
ax[3].plot(telemetry_driver_3['Distance'], telemetry_driver_3['Brake'], label=driver_3,
           color=ff1.plotting.team_color(team_driver_3))
ax[3].set(ylabel='Brake')
# Gear trace
ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1,
           color=ff1.plotting.team_color(team_driver_1))
ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2,
           color=ff1.plotting.team_color(team_driver_2))
ax[4].plot(telemetry_driver_3['Distance'], telemetry_driver_3['nGear'], label=driver_3,
           color=ff1.plotting.team_color(team_driver_3))
ax[4].set(ylabel='Gear')

# RPM trace
ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1,
           color=ff1.plotting.team_color(team_driver_1))
ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2,
           color=ff1.plotting.team_color(team_driver_2))
ax[5].plot(telemetry_driver_3['Distance'], telemetry_driver_3['RPM'], label=driver_3,
           color=ff1.plotting.team_color(team_driver_3))
ax[5].set(ylabel='RPM')

# DRS trace
ax[6].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=driver_1,
           color=ff1.plotting.team_color(team_driver_1))
ax[6].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=driver_2,
           color=ff1.plotting.team_color(team_driver_2))
ax[6].plot(telemetry_driver_3['Distance'], telemetry_driver_3['DRS'], label=driver_3,
           color=ff1.plotting.team_color(team_driver_3))
ax[6].set(ylabel='DRS')
ax[6].set(xlabel='Lap distance (meters)')
"""
# Hide x labels and tick labels for top plots and y ticks for right plots.

for driver in testingSession.drivers:
    plt.axhline(0)
    telemetry_driver_n = testingSession.laps.pick_driver(driver).pick_fastest().get_telemetry().add_distance()
    plt.plot(telemetry_driver_n["Distance"], telemetry_driver_n['RPM'], label= driver, color=ff1.plotting.team_color(testingSession.laps.pick_driver(driver).pick_fastest()['Team']))
plt.ylabel='RPM'

# Store figure
plt.savefig(plot_filename, dpi=300)
plt.show()
PP = PdfPages("2023Pre-SeasonTesting-Practice1-ALOVSZHO.pdf")


