pipeline {
  agent any
  stages {
    stage ("build") {
      steps {
        echo "let's mess up"
      }
    }
    stage ("test") {
      steps {
        echo "let's ignore bug"
      }
    }
    stage ("deploy") {
      steps {
        echo "let's fail"
      }
    }
  }
}