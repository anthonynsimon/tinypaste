from shorten_id_api import app, config, manager

@manager.command
def run():
    """Run the Shorten ID API server from the dotenv config"""
    app.run(
            debug=config.DEBUG,
            host=config.APP_HOST,
            port=config.APP_PORT
        )

if __name__ == '__main__':
    manager.run()