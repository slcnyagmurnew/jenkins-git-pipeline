pipeline {
    agent any
    stages {
        stage('build') {
	    steps {
		script {
		    try {
		        sh 'python3 gcd.py'
		        echo 'Built successfully!'
	            }
	            catch (err) {
		        echo 'Can not build!'
	            }
		}
	    }
        }
	stage('test') {
	    steps {
		script {
		    try {
		        sh 'nc -vz 127.0.0.1 32000'
	            }
	            catch (err) {
			echo 'Sleep required, wait a moment..'
	            }
		    echo 'Wait Completed !'
		}
		sh 'python3 -m pytest tests'
		echo 'Test Passed
	    }
	}
    }
}
