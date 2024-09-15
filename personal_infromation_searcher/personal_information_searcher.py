import requests
import os, sys, getopt
from requests.auth import HTTPBasicAuth

splunkHost = "splunk.app.internal.net"

usageText = "personal_information_searcher.py --team <team> --environment <environment> --applicationName <applicationName> --from <fromEpoch> --to <toEpoch> data to find"

def main(args):
    fromDate = ""
    toDate = ""
    team = ""
    applicationName = ""
    environment = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hf:t:e:c:a:",["help", "from=", "to=", "environment=", "team=", "applicationName="])
    except getopt.GetoptError:
        print(usageText)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(usageText)
            sys.exit()
        elif opt in ("-f", "--from"):
            fromDate = arg
        elif opt in ("-t", "--to"):
            toDate = arg
        elif opt in ("-e", "--environment"):
            environment = arg
        elif opt in ("-c", "--team"):
            team = arg
        elif opt in ("-a", "--applicationName"):
            applicationName = arg

    splunkAuth = HTTPBasicAuth(os.environ["splunkUsername"], os.environ["splunkPassword"])

    for searchString in args:
        requestParams = {
            "index_earliest": fromDate,
            "index_latest": toDate,
            "search": f"search index=\"{team}-{environment}-app\" source=\"{team}.{environment}.app.{applicationName}\" \"{searchString}\"",
            "output_mode": "json_rows",
            "exec_mode": "oneshot"
        }

        response = requests.post(f"https://{splunkHost}:8089/services/search/jobs/export", auth=splunkAuth, data=requestParams, verify=False)

        if response.status_code != 200:
            print(f"There was a problem conducting the search. HTTP Status from Splunk was: {response.status_code}, {response.text}")
            exit(1)

        if response.text != '' and 'rows' in response.json() and len(response.json()['rows']) > 0 :
            print(f"The search for PI resulted in a match. Please open the following link: https://{splunkHost}:8000/en-GB/app/search/search?q={requests.utils.quote(requestParams['search'])}")
            exit(1)

        print(f"Search for word {searchString} completed successfully, no results found")

if __name__ == "__main__":
    main(sys.argv)