import os


def get_config_from_environment(env_content):
    env_content += "FINMIND_USER={}\n".format(
        os.environ.get("FINMIND_USER", "")
    )
    env_content += "FINMIND_PASSWORD={}\n".format(
        os.environ.get("FINMIND_PASSWORD", "")
    )
    env_content += "FINMIND_API_TOKEN={}\n".format(
        os.environ.get("FINMIND_API_TOKEN", "")
    )
    return env_content


env_content = ""
env_content = get_config_from_environment(env_content)

with open(".env", "w", encoding="utf8") as env:
    env.write(env_content)
