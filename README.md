# CI Helper Functions

This repo I plan to use to share some common CI scripts I've created over the years.

## Personal Information Searcher

The logging of sensitive information can present a lucrative target for adversaries. Logs, and the systems that are used to access them are often left without the extra protections that are afforded to operational databases and applications.

Logs also form the basis for audit, and must be protected from tampering or deletion. It's for this reason, that once PI is logged, it's very difficult (and against common practice) to manipulate that data and remove the sensitive information from the logs.

So, the best cure is prevention.

This is a Jenkins function I created to help search Splunk after the run of any automation test scripts. Our automation scripts create their own test data, which can be then passed to this script via command line arguments and perform splunk searches for that application data. If data is found, the recent application changes have included a logging change that's exposed one or more of these sensitive fields, and this script will return a non-zero response code, automatically marking a failure in most CI systems.
