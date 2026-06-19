# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Constants
# g = 9.81
# L1, L2 = 1.0, 1.0
# m1, m2 = 1.0, 1.0
# dt = 0.02

# # Initial conditions
# theta1 = np.pi / 2
# theta2 = np.pi / 2
# omega1 = 0
# omega2 = 0

# trail_x = []
# trail_y = []

# # Physics equations
# def derivatives(state):
#     t1, w1, t2, w2 = state
#     delta = t2 - t1

#     den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
#     den2 = (L2 / L1) * den1

#     a1 = (
#         m2 * L1 * w1**2 * np.sin(delta) * np.cos(delta)
#         + m2 * g * np.sin(t2) * np.cos(delta)
#         + m2 * L2 * w2**2 * np.sin(delta)
#         - (m1 + m2) * g * np.sin(t1)
#     ) / den1

#     a2 = (
#         -m2 * L2 * w2**2 * np.sin(delta) * np.cos(delta)
#         + (m1 + m2) * (
#             g * np.sin(t1) * np.cos(delta)
#             - L1 * w1**2 * np.sin(delta)
#             - g * np.sin(t2)
#         )
#     ) / den2

#     return np.array([w1, a1, w2, a2])

# # Initial state
# state = np.array([theta1, omega1, theta2, omega2])

# # Figure setup
# fig, ax = plt.subplots(figsize=(7,7))
# ax.set_xlim(-2.2, 2.2)
# ax.set_ylim(-2.2, 2.2)
# ax.set_aspect('equal')
# ax.grid()

# line, = ax.plot([], [], 'o-', lw=2)
# trail, = ax.plot([], [], lw=1)

# def update(frame):
#     global state

#     # Euler integration
#     state += derivatives(state) * dt

#     t1, _, t2, _ = state

#     # Positions
#     x1 = L1 * np.sin(t1)
#     y1 = -L1 * np.cos(t1)

#     x2 = x1 + L2 * np.sin(t2)
#     y2 = y1 - L2 * np.cos(t2)

#     trail_x.append(x2)
#     trail_y.append(y2)

#     line.set_data([0, x1, x2], [0, y1, y2])
#     trail.set_data(trail_x, trail_y)

#     return line, trail

# ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=True)

# plt.show()


import turtle, math

s=turtle.Screen()
s.bgcolor("black")
s.setup(900,900)
s.tracer(0)

p=turtle.Turtle()
p.hideturtle()
p.speed(0)
p.pensize(2)
p.pencolor("cyan")

L=[120,100,80]
A=[0.5,1.0,1.5]
V=[0,0,0]
g=0.08

while True:
    x=y=0
    for i in range(3):
        V[i]+=(-g*math.sin(A[i])+0.01*math.sin(A[i-1]-A[i] if i else 0))
        A[i]+=V[i]
        x+=L[i]*math.sin(A[i])
        y-=L[i]*math.cos(A[i])

    p.goto(x,y)
    p.dot(2)

    s.update()