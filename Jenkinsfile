pipeline
   agent any
      stages('git clone') {
          stage {
              git clone , branch: main
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
