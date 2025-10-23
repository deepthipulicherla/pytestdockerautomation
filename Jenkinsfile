pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/deepthipulicherla/pytestdockerautomation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("pytest-runner")
                }
            }
        }

        stage('Run Tests in Container') {
            steps {
                script {
                    dockerImage.run("-v $WORKSPACE/reports:/app/reports")
                }
            }
        }
         stage('Send Email') {
    steps {
        emailext (
            subject: "Pytest Report",
            body: "Test execution completed. Please find the attached HTML report.",
            to: "deepthi1987.p@gmail.com",
            attachLog: false,
            attachmentsPattern: "report.html"
        )
    }
}
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
