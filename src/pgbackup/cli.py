import argparse

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Backup PostgreSQL databses locally or to AWS S3 bucket
    """
    )
    parser.add_argument('url', help='URL of database to backup')
    parser.add_argument('--driver',
            help='how and where to store backup',
            nargs=2,
            metavar=("DRIVER", "DESTINATION"),
            action=DriverAction,
            required=True
            )

    return parser

parser = create_parser()
parser.parse_args()
