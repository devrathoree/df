pipeline {
    agent any
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
                    bin/ 'python manage.py runserver'
                }
            }
        }
    }
}
