pipeline {
    agent {label 'node1'}

    stages {
        stage("1.git") {
            steps {
               git credentialsId: 'github_credentials', url: 'https://github.com/aabhinnav1999/DevOpsSec_project'
            }
        }
        stage("2.pwd") {
            steps {
                sh "pwd"
            }
        }
        
    }
}