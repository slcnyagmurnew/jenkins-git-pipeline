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
		sh 'python3 -m pytest tests'
		echo 'Test Passed'
	    }
	}
    }
}
