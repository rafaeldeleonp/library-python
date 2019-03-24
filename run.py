from library import app
import logging as logger

logger.basicConfig(level="DEBUG")

app.config.from_pyfile('config.py')

if __name__ == '__main__':
    logger.debug("Starting the application on port: %s" % (app.config["PORT"]))
    app.run(host=app.config["HOST"], port=app.config["PORT"])
