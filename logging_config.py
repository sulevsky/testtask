LOGGING_CONFIGURATION = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailedFormatter": {
            "class": "logging.Formatter",
            "format": "%(asctime)s %(levelname)-8s %(name)s %(funcName)s() %(message)s  call_trace=%(pathname)s L%(lineno)-4d",
        },
    },
    "handlers": {
        "detailedConsoleHandler": {
            "class": "logging.StreamHandler",
            "formatter": "detailedFormatter",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["detailedConsoleHandler"],
            "level": "INFO",
        },
    },
}
