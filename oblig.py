import matplotlib.pyplot as plt
import numpy as np

# Funksjonen f(x) som skal analyseres
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# Den deriverte av f(x)
def g(x):
    return -1/4 * np.exp(-x/4) * np.arctan(x) + np.exp(-x/4) * 1/(1 + x**2)

# Der den deriverte g(x) er lik 0, finner vi ekstremalpunktene til f(x). 
# Vi kan bruke halveringsmetoden for å finne nullpunktet til g(x).
# a og b er startpunktene for intervallet, og tol er toleransen for hvor nøyaktig vi ønsker svaret.
def halveringsmetoden(a, b, tol):
    while True:
        mid = (a + b) / 2
        g_mid = g(mid)
        if abs(g_mid) < tol:
            return mid
        elif g(a) * g_mid < 0:
            b = mid
        else:
            a = mid

# Ved å se på plottet ser man at det ligger mellom 0 og 3 et sted. Toleransen er lik 1 * 10^-5 for å få et nøyaktig svar.
print(halveringsmetoden(0, 3, 1e-5))


# Mellom x = -1 og x = 10 lager den 1000 punkter. Dette gir en jevn kurve for både f(x) og g(x) når de plottes.
x = np.linspace(-1, 10, 1000)

plt.plot(x, f(x), label='f(x)')
plt.plot(x, g(x), label='g(x)')
plt.title('Plot of f(x) = exp(-x/4) * arctan(x) and g(x) = f\'(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
