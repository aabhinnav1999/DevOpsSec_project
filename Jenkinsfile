pipeline {
    agent {label 'node_1'}
    stages {
        stage("1.git") {
            steps {
               git credentialsId: 'github_credentials', url: 'https://github.com/aabhinnav1999/DevOpsSec_project'
            }
        }
        // stage('2.restart') {
        //     steps {
        //         sh '''sudo systemctl daemon-reload
        //             sudo systemctl restart gunicorn
        //             sudo systemctl restart nginx'''
        //     }
        // }        
    }
}