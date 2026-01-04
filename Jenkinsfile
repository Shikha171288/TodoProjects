pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Shikha171288/TodoProjects.git'
            }
        }

        stage('Backend - Install Dependencies') {
            steps {
                dir('backend') {
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\pip install -r requirements.txt'
                }
            }
        }

        stage('Backend - Syntax Check') {
            steps {
                dir('backend') {
                    bat 'venv\\Scripts\\python -m py_compile app.py'
                }
            }
        }

        stage('Frontend - Install Dependencies') {
            steps {
                dir('frontend') {
                    bat 'npm install'
                }
            }
        }

        stage('Frontend - Build') {
            steps {
                dir('frontend') {
                    bat 'npm run build'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build successful!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
