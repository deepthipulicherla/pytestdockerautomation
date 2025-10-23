pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/your-repo.git'  // Replace with your repo
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pytest-runner .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --name pytest-runner pytest-runner'
            }
        }

        stage('Copy Report') {
            steps {
                sh 'docker cp pytest-runner:/app/reports/report.html ./reports/report.html'
            }
        }
         stage('Send Email') {  //Install Email Extension Plugin Configure SMTP in Manage Jenkins → Configure System → Extended E-mail Notification Use emailext for rich email formatting and attachments
            steps {
                emailext (
                    subject: "Pytest Report",
                    body: "Test execution completed. Please find the attached HTML report.",
                    to: "team@example.com",
                    attachLog: false,
                    attachmentsPattern: "report.html"
                )
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
        }
    }
}
