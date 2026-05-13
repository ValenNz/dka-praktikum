import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality['poor'] = fuzz.trapmf(quality.universe, [0, 0, 2, 5])
quality['average'] = fuzz.trapmf(quality.universe, [0, 4, 6, 10])
quality['good'] = fuzz.trapmf(quality.universe, [5, 8, 10, 10])

service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trapmf(service.universe, [0, 4, 8, 10])
service['good'] = fuzz.trimf(service.universe, [5, 10, 10])

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

quality.view()
service.view()
tip.view()

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(quality['good'] | service['good'], tip['high'])

tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tip_simulation = ctrl.ControlSystemSimulation(tip_ctrl)

tip_simulation.input['quality'] = 6
tip_simulation.input['service'] = 8

tip_simulation.compute()

print("Nilai Tip:", tip_simulation.output['tip'])

tip.view(sim=tip_simulation)

plt.show()