pipeline
   agent any
      stages('git clone') {
          stage {
              git clone 'https://github.com/swatiV-27/docker-jenkins-staticwebsite.git' , branch: main
          }
      }
       stages('docker build') {
         stage {    
         sh 'docker build -t image-devops .'
       }
     }
       stages('previous container delete') {
         stage {
              sh 'docker rm -f devops-con'
         }
       }
       stages('container bhuild') {
           sh '''
                docker run -d \
                -p 5000:5000 \
                --name devops-con \
                image-devop
              '''
       }
     }
      stages('check container') {
        stage {
             sh 'docker ps'
        }
      }
    }
}
