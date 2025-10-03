#Solves second order linear homogeneous differential equations with constant coefficients:
#   " x''(t) + b*x'(t) + c*x(t) = 0"

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def get_float(prompt):
    #Richiede un input numerico con controllo degli errori
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Inserisci un numero valido!")


def solve_ode(b, c, A=1.0, B=1.0, t_range=(0, 10), n_points=400):
    #Risolvi e plott la soluzione generale dell'ODE
    t = sp.symbols('t')
    d = b**2 - 4*c  # discriminante

    if d > 0:
        # due radici reali distinte
        r1 = (-b + d**0.5) / 2
        r2 = (-b - d**0.5) / 2
        x = A*sp.exp(r1*t) + B*sp.exp(r2*t)
        sol_type = f"Reali distinte: r1={r1:.3f}, r2={r2:.3f}"
    elif d == 0:
        # radice reale doppia
        r = -b / 2
        x = (A + B*t)*sp.exp(r*t)
        sol_type = f"Reale doppia: r={r:.3f}"
    else:
        # radici complesse
        alpha = -b / 2
        beta = (-d)**0.5 / 2
        x = sp.exp(alpha*t)*(A*sp.cos(beta*t) + B*sp.sin(beta*t))
        sol_type = f"Complesse: α={alpha:.3f}, β={beta:.3f}"

    # conversione a funzione numerica
    x_func = sp.lambdify(t, x, modules=['numpy'])
    t_vals = np.linspace(t_range[0], t_range[1], n_points)
    x_vals = x_func(t_vals)

    # plot
    plt.figure(figsize=(8, 4))
    plt.plot(t_vals, x_vals, label=sol_type)
    plt.title("General Solution of the Differential Equation")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"✅ Soluzione generale trovata ({sol_type})")
    print("   La forma generale è:")
    sp.pprint(x)


if __name__ == "__main__":
    print("=== Risolutore ODE: x''(t) + b*x'(t) + c*x(t) = 0 ===")
    b = get_float("Inserisci b: ")
    c = get_float("Inserisci c: ")
    A = get_float("Costante A (default=1): ") or 1.0
    B = get_float("Costante B (default=1): ") or 1.0

    solve_ode(b, c, A, B)
