pipeline {
    agent {label 'node_1'}
    stages {
        stage("1.git") {
            steps {
               git credentialsId: 'github_credentials', url: 'https://github.com/aabhinnav1999/DevOpsSec_project'
            }
        }
        stage("2.build") {
            steps {
                sh '''#!/bin/bash
                    source env/bin/activate
                    pip install -r requirements.txt'''
            }
        }
        
        stage('4.restart') {
            steps {
                sh '''sudo systemctl daemon-reload
                    sudo systemctl restart gunicorn
                    sudo systemctl restart nginx'''
            }
        } 

        stage("3.test") {
            steps {
                sh '''#!/bin/bash
                    source env/bin/activate
                    python3 -m pylint *.py'''
            }
        } 
              
    }
}