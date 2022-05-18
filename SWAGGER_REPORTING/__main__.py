#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Reporting Service'}, pythonic_params=True)
    app.run(port=6005)


if __name__ == '__main__':
    main()
