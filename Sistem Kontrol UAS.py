import matplotlib.pyplot as plt
import control as ctrl

# Definisikan sistem
num = [2]
den = [1, 5, 6, 2]
system = ctrl.TransferFunction(num, den)

# Root Locus
plt.figure()
ctrl.rlocus(system)
plt.title('Root Locus')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.grid(True)
plt.show()

# Nyquist
plt.figure()
ctrl.nyquist(system)
plt.title('Nyquist Plot')
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.grid(True)
plt.show()

# Tuning PID menggunakan Ziegler-Nichols
K_u = 18
P_u = 2.565

K_p = 0.6 * K_u
K_i = 2 * K_p / P_u
K_d = K_p * P_u / 8

pid = ctrl.TransferFunction([K_d, K_p, K_i], [1, 0])

# Sistem tertutup dengan PID
closed_loop_system = ctrl.feedback(pid * system, 1)

# Simulasi step response
t, y = ctrl.step_response(closed_loop_system)

plt.figure()
plt.plot(t, y)
plt.title('Step Response with PID Controller')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.grid(True)
plt.show()
