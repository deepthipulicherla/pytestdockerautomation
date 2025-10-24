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
                sh 'docker run --rm -v $WORKSPACE:/app pytest-runner'
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
