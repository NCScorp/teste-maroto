node('master') {
    stage('Checkout') {
			
        timeout(time: 3600, unit: 'SECONDS') {
            checkout scm
        }
    }

    stage('script'){
	bat "echo 'salve' > teste"
        bat "dir ${env.WORKSPACE}"
    }

    stage('Clean') {
        deleteDir()
    }
}
