import os


def get_secret(secret: str, env_var: str) -> str:
    if os.environ.get(env_var):
        return os.environ.get(env_var)
    f = open(f"/var/openfaas/secrets/{secret}", "r")
    return str(f.read())
