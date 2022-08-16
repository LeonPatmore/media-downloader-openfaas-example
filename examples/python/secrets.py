
def get_secret(secret: str) -> str:
    f = open(f"/var/openfaas/secrets/{secret}", "r")
    return str(f.read())
