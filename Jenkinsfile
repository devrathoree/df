pipeline {
    agent {
        node {
            customWorkspace '/home/dev/df'
        }
    }
    stages {
        stage('Checkout project') {
            steps {
                script {
                    git branch: "main",

                        url: 'https://github.com/devrathoree/df.git'
                }
            }
        }
        stage('Installing packages') {
            steps {
                script {
                    sh 'python manage.py runserver'
                }
            }
        }
    }
}
