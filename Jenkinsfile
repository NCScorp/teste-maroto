node('master') {
    stage('Checkout') {
			
        timeout(time: 3600, unit: 'SECONDS') {
            checkout scm
        }
    }

    stage('script'){
        bat "dir ${env.WORKSPACE}\\output"
    }

    stage('Clean') {
        deleteDir()
    }
}