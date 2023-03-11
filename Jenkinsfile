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

    stage('up to s3'){
        withAWS(credentials: 'JENKINS_SP_UPLOAD', region: 'sa-east-1') {
            def bucket = env.BUCKET_CDN
            def file = "${env.WORKSPACE}\\output\\teste"
            def destination = "testezim/teste"
            
            bat "python utils\\sas.py -f ${file} -b ${bucket} -d ${destination}"
        }

    stage('Clean') {
        deleteDir()
    }
}
