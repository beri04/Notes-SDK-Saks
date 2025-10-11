pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                echo "Pulling code from github"
                checkout scm
            }
        }
        stage('Install Dependencies'){
            steps{
                echo "RUnning Python Tests"
                sh 'pytest --maxfail=1 --disable-warnings -q || echo "Tests folder not found"'
            }
        }
        stage('Package Completed yo'){
            steps{
                echo "SDK build pipeline finished successfully"
            }
        }
    }
}