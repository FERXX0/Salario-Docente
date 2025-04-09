pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'apt update && apt install -y python3 python3-pip'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 test_funcion.py'
            }
        }
    }

    post {
        success {
            echo '✅ Todas las pruebas pasaron desde GitHub'
        }
        failure {
            echo '❌ Fallaron las pruebas desde GitHub'
        }
    }
}