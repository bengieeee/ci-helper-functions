pipeline {
    agent none
    stages {
        stage('PI Searching Example') {
            node('python-312') {
                withCredentials([
                    string(credentialsId: '/splunkUsername', variable: 'splunkUsername'),
                    string(credentialsId: '/splunkPassword', variable: 'splunkPassword')
                ]) {
                    sh "pip install pipenv"
                    sh "pipenv install"
                    sh "pipenv run python3 ./personalInformationSearcher.py --team ${config.application.team} --environment ${config.environment} --applicationName ${config.application.name} --from ${config.startEpoch} --to now \'emailtesting@test-data.com\' NADA 91500000 \'TEST ADDRESS LINE 1\' \'TEST ADDRESS LINE 2\' Redfern \'TEST Bus ADDRESS LINE 1\' \'TEST Bus ADDRESS LINE 2\' 1980-05-01"
                }
            }
        }
    }
}
