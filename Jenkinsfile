pipeline {
  agent any

  parameters {
    choice(name: 'PYTHON_VERSION', choices:['3.9', '3.7'], description:'choose your python version' )
  }

  stages {
    stage('initiate'){
      steps {
        script {
          if (env.PYTHON_VERSION == ''){
            env.PYTHON_VERSION = 3.9
            sh 'echo "[Reseting] PYTHON_VERSION: $PYTHON_VERSION"'
          }
          env.IMAGE_NAME = "python:$PYTHON_VERSION-alpine"
          echo "IMAGE_NAME: $IMAGE_NAME"
          echo "env.IMAGE_NAME: ${env.IMAGE_NAME}"
          echo "PYTHON_VERSION: $PYTHON_VERSION"
        }
      }
    }
    stage ("test") {
      steps {
        sh '''
          echo "testing below variables"
          hostname
          hostname -i
          whoami
          echo "image name is: $IMAGE_NAME"
          echo "PYTHON_VERSION is: $PYTHON_VERSION"
        '''
      }
    }
    stage('dockering'){
      agent {
        docker {
          image "$IMAGE_NAME"
        }
      }
      environment {
        PERSONAL_ACCESS_TOKEN = credentials('PERSONAL_ACCESS_TOKEN')
      }
      steps {
        script {
            sh '''
              echo "with docker"
              hostname
              hostname -i
              python --version
              which python
              echo "image name is: $IMAGE_NAME"
              ls -ltrh
              mkdir -p ./project
              cd ./project
            '''
            git branch: 'main', url: 'https://github.com/Rony-dot/actions_in_action.git'
            sh '''
              ls -ltrh
              export PYTHONUSERBASE=/tmp/python_packages
              python -m pip install --upgrade --user pip
              if [ -f requirements.txt ]; then pip install --user -r requirements.txt; fi
              export PATH=$PYTHONUSERBASE/bin:$PATH
              export MY_ENV_VAR=$MY_SECRET  # Set the environment variable using the secret
              python src/github_api.py
            '''
          }
      }
    }
    // stage ("build") {
    //   steps {
    //     echo "let's mess up"
    //     git branch: 'main', url: 'https://github.com/Rony-dot/actions_in_action.git'
    //     sh 'echo "listing git directory"; ls -ltrh'
    //     sh 'echo "listing git nested directories"; ls -ltrh *'
    //   }
    // }
  }
}
