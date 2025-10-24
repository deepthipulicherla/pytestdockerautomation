pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pytest-runner .'
            }
        }

        stage('Run Tests') {
    steps {
        sh 'docker create --name temp-runner pytest-runner'
        sh 'docker cp temp-runner:/app/reports/report.html reports/report.html'
        sh 'docker rm temp-runner'
    }
}

        stage('Send Email') {
            steps {
                emailext (
                    subject: "Pytest Report",
                    body: "Test execution completed. Please find the attached HTML report.",
                    to: "deepthi1987.p@gmail.com",
                    attachLog: false,
                    attachmentsPattern: "reports/report.html"
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
