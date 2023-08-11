from balena import Balena

token = "lYiTWEpwpPLbcdMeTapewfpfgybZUXPe"

balena = Balena()
credentials = {'username':'vveirs@coloradocollege.edu', 'password':'z#XIb9iPh0^2'}
balena.auth.login(**credentials)

x =balena.models.application.env_var.get('vveirs/val-one', 'foo')
print("in getvarsBalenaToken.py : foo from fleet =", x)
y =balena.models.device.env_var.get('c07e57f', 'bar')
print("device variable is",y)
y =balena.models.device.env_var.get('c07e57f', 'test')
print("device variable is",y)


