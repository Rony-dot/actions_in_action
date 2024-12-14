pipeline {
  agent any
  stages {
    stage ("build") {
      steps {
        echo "let's mess up"
        git branch: 'main', url: 'https://github.com/Rony-dot/actions_in_action.git'
        sh 'echo "listing git directory"; ls -ltrh'
        sh 'echo "listing git nested directories"; ls -ltrh *'
      }
    }
    stage ("test") {
      steps {
        echo "let's ignore bug"
        sh 'echo "listing git directory"; ls -ltrh'
      }
    }
    stage ("deploy") {
      steps {
        echo "let's fail"
        sh 'python src/github_api.py'
      }
    }
  }
}
