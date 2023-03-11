node('master') {
    stage('Checkout') {
			
        timeout(time: 3600, unit: 'SECONDS') {
            checkout scm
        }
    }

    stage('script'){
	bat "mkdir output"
	bat "echo 'salve' > output\\teste"
        bat "dir ${env.WORKSPACE}"
	bat "dir ${env.WORKSPACE}\\output"
    }

    stage('Clean') {
        deleteDir()
    }
}
