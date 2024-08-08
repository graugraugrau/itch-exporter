pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build'
        }
    }

    stages {
        stage('Install')
        {
            steps {
                sh 'pipenv install --dev --system'
            }
        }
        stage('Lint')
        {
            steps {
                sh 'task lint'
            }
        }
        stage('Type')
        {
            steps {
                sh 'task type'
            }
        }
        stage('Test')
        {
            steps {
                sh 'task test'
            }
        }
        stage('Release')
        {
            when
            {
                branch 'main'
            }
            steps {
                script
                {
                    docker.withRegistry('', 'DOCKER_HUB_REGISTRY')
                    {
                        docker.build("dunkelgrau/itch-exporter:latest").push()
                    }
                }
            }
        }
    }
}
