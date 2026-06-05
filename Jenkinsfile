pipeline
   agent any
      stages {
          stage ('Git Clone') {
              steps {
                    git branch: 'main',
                    url: 'https://github.com/swatiV-27/docker-jenkins-staticwebsite.git'
         }
      }
       stage('docker build') {
         steps {    
         sh 'docker build -t image-devops .'
       }
     }
       stage('previous container delete') {
         steps {
              sh 'docker rm -f devops-con || true'
         }
       }
       stage('container bhuild') {
           steps {
              sh '''
                docker run -d \
                -p 5000:5000 \
                --name devops-con \
                image-devops
              '''
       }
     }
      stage('check container') {
        steps {
             sh 'docker ps'
        }
      }
    }
}
