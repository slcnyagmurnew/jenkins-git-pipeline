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
		sh 'pip3 install pytest'
	        script {
		    try {
			sh 'python3 -m pytest tests'
			echo 'Test Passed'
		    }
		    catch (err) {
			echo 'Tests not passed!'
			sh 'git checkout dev'
			sh 'git reset --hard HEAD~1'
			sh 'git push -f origin dev'
			echo 'Test Failed ! Changes Reverted !'
		    }
		}
	    }
	}
    }
}
