pipeline {
agent any

stages {
    stage('Checkout (Ingredientes)') {
        steps {
            echo 'Descargando la receta de BurgerCode...'
            checkout scm
        }
    }

    stage('Build (Cocinar)') {
        steps {
            echo 'Cocinando la imagen Docker...'
            sh 'docker build -t burgercode-app .'
        }
    }

    stage('Test (Control de Calidad)') {
        steps {
            echo 'Probando la hamburguesa...'
            // Ejecutamos el test DENTRO del contenedor para asegurar consistencia
            sh 'docker run --rm burgercode-app python test.py'
        }
    }

    stage('Deploy (Entrega)') {
        steps {
            echo 'Desplegando en Producción...'
            // Detenemos el contenedor anterior si existe para evitar conflictos de puerto
            sh 'docker rm -f burger-prod || true'
            sh 'docker run -d --name burger-prod -p 5000:5000 burgercode-app'
            echo '¡Hamburguesa servida en http://localhost:5000!'
        }
    }
}

post {
    always {
        echo 'Limpiando la cocina...'
        // Elimina imágenes intermedias para ahorrar espacio en el Windows virtualizado
        sh 'docker image prune -f'
    }
    success {
        echo '¡Pipeline completado con éxito! La hamburguesa está lista.'
    }
    failure {
        echo '¡ALERTA! El pipeline ha fallado. Revisa los logs de Jenkins.'
    }
}


}
