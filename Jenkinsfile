pipeline {
    agent {
        docker { image 'python:3' }
    }
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
		sh 'pip3 install pytest'
		sh 'python3 -m pytest tests'
		echo 'Test Passed'
	    }
	}
    }
}
