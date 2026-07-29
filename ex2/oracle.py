import os
from dotenv import load_dotenv

load_dotenv()

KEYS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]


def _get_config() -> tuple[dict[str, str | None], list[str]]:
    config: dict[str, str | None] = {}
    warnings: list[str] = []
    for key in KEYS:
        value = os.environ.get(key)
        if value is None:
            warnings.append(f"{key} not set")
        config[key] = value
    return config, warnings


def _database(url: str | None) -> str:
    if not url:
        return "No connection configured"
    if "localhost" in url or "127.0.0.1" in url:
        return "Connected to local instance"
    return "Connected to remote instance"


def _api(key: str | None) -> str:
    return "Authenticated" if key else "No Authentication key found "


def _zion(endpoint: str | None) -> str:
    return "Online" if endpoint else "Offline - no endpoint configured"


def _env_configured(env_path: str) -> bool:
    if not os.path.isfile(env_path):
        return False
    with open(env_path, "r") as f:
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and "=" in stripped:
                return True
    return False


def _security_check(config: dict[str, str | None]) -> None:
    env_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ".env"
    )
    source_path = os.path.abspath(__file__)

    no_hardcoded = True
    with open(source_path, "r") as f:
        for line in f:
            stripped = line.strip()
            is_secret_line = stripped.startswith(
                ("API_KEY=", "DATABASE_URL=")
            )
            if is_secret_line and "os.environ" not in stripped:
                no_hardcoded = False
                break

    if no_hardcoded:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] hardcoded secrets detected!")

    if _env_configured(env_path):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not configured")

    mode = config['MATRIX_MODE']
    if mode is None:
        print("[KO] Unknown mode running (MATRIX_MODE not set)")
    elif mode.lower() == "development":
        print("[OK] Production overrides available")
    elif mode.lower() == "production":
        print("[OK] Production mode currently running!")
    else:
        print("[KO] Unknown mode running")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config, warnings = _get_config()

#    API_KEY="test-hardcoded-key"

    if warnings:
        print("Configuration warnings:")
        for warning in warnings:
            print(f" [!] {warning}")
        print()

    print("Configuration loaded:")
    print(f" Mode: {config['MATRIX_MODE']}")
    print(f" Database: {_database(config['DATABASE_URL'])}")
    print(f" API Access: {_api(config['API_KEY'])}")
    print(f" Log Level: {config['LOG_LEVEL']}")
    print(f" Zion Network: {_zion(config['ZION_ENDPOINT'])}\n")

    print("Environment security check:")
    _security_check(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
