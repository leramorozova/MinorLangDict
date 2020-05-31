class ConfigError(Exception):
    def __init__(self, field):
        msg = f"No required field in config: {field} is required"
        super().__init__(msg)
