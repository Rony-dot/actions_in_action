pipeline {
  agent any

  stages {
    stage('build w/ docker'){
      agent {
        dockerfile {
          filename 'Dockerfile.jenkins'
          label 'custom-dockerimage'
          reuseNode true
        }
      }
      environment {
        PERSONAL_ACCESS_TOKEN = credentials('PERSONAL_ACCESS_TOKEN')
      }
      steps {
        script {
            sh '''
              echo "______________________________[stage]: build w/ docker______________________________"
              hostname
              hostname -i
              python --version
              which python
              echo "image name is: $IMAGE_NAME"
            '''
            git branch: 'main', url: 'https://github.com/Rony-dot/actions_in_action.git'
            sh '''
              export PYTHONUSERBASE=/tmp/python_packages
              python -m pip install --upgrade --user pip
              if [ -f requirements.txt ]; then pip install --user -r requirements.txt; fi
              export PATH=$PYTHONUSERBASE/bin:$PATH
              export MY_ENV_VAR=$MY_SECRET  # Set the environment variable using the secret
              #python src/github_api.py
            '''
          }
      }
    }
    stage ("test w/ docker") {
      agent {
        dockerfile {
          filename 'Dockerfile.jenkins'
          label 'custom-dockerimage'
          reuseNode true
        }
      }
      steps {
        sh '''
          echo "______________________________[stage]: test w/ docker______________________________"
          export PYTHONUSERBASE=/tmp/python_packages
          pytest --junitxml=./junit.xml
        '''
        junit 'junit.xml'
        cleanWS()
      }
    }
  }
  // post {
  //   always {
  //     junit 'junit.xml'
  //   }
  // }
}
