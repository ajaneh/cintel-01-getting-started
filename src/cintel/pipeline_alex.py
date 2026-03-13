# === DECLARE IMPORTS ===

# First from the Python standard library (no installation needed)
import logging
from pathlib import Path

# Then, external dependencies (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P1", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Path = Path.cwd()
DOCS_DIR: Path = ROOT_DIR / "docs"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("main has initialized successfully!")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DOCS_DIR", DOCS_DIR)

    LOG.info("LOGGER is configured correctly!")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
