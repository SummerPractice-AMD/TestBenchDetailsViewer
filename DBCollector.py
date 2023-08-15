import argparse
from generatejson import parsedir, parsefile
from introducereDB import DatabaseLoader
import yaml


def load_config(config_file):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config


def connect_to_database(config):
    database_host = config["regression_details"]["database_host"]
    database_port = config["regression_details"]["database_port"]
    database_name = config["regression_details"]["database_name"]
    connection_string = "mongodb://" + database_host + ":" + str(database_port)
    return DatabaseLoader(connection_string, database_name)


def parse_command_line():
    parser = argparse.ArgumentParser(description="Collect and load test run data into MongoDB")
    parser.add_argument("--dir",  help="Specify the directory containing test run files")
    parser.add_argument("--file", help="Specify the test run file")
    return parser.parse_args()


def main():
    args = parse_command_line()

    config = load_config("config.yml")
    loader = connect_to_database(config)

    if args.dir:
        json_output = parsedir(args.dir)
        loader.load_from_json_list(json_output)
    elif args.file:
        json_output_from_file = parsefile(args.file)
        loader.load_from_json(json_output_from_file)
    else:
        print("Specify either --dir or --file option.")
   
        
if __name__ == "__main__":
    main()