def res = "success"
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
			res = "fail"
			echo 'Tests not passed!'
			sh 'git checkout dev'
			sh 'git pull'
			sh 'git reset --soft HEAD~1'
			echo 'Test Failed ! Changes Reverted !'
		    }
		    finally {
			if (res == "fail") {
			    withCredentials([gitUsernamePassword(credentialsId: 'ed19ce27-d1d6-41ab-bb35-708be91e1971', gitToolName: 'git-tool')]) {
                    	        sh 'git push -f origin dev'
                	    }
			} else {
			    echo 'Executed build and tests successfully finished!'
			}
		    }
		}
	    }
	}
    }
}
