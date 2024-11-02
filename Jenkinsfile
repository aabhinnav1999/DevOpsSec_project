pipeline {
    agent {label 'node_1'}

    stages {
        stage('1.git') {
            steps {
                git credentialsId: 'github_credentials', url: 'https://github.com/aabhinnav1999/DevOpsSec_project'
            }
        }
        stage('2.scripts.sh') {
            steps {
                sh '''sudo chmod +x scripts.sh
                ./scripts.sh'''
            }
        }
        stage('3.nginx') {
            steps {
                sh '''cd nginx
                sudo chmod +x nginx.sh
                ./nginx.sh'''
            }
        }
    }
}