pipeline {
    agent none
    options { timeout(time: 2, unit: 'HOURS') }
    stages {
        stage('UI Testing Stage') {
            agent { label 'UI-Testing' }
            steps {
                cleanWs()
                checkout scm
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest tests/test_ui.py --html=reports/ui_report.html --self-contained-html || true
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'ui_report.html',
                        reportName: 'UI Execution Report'
                    ])
                }
            }
        }
        stage('API Testing Stage') {
            agent { label 'API-Testing' }
            steps {
                cleanWs()
                checkout scm
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest tests/test_api.py --html=reports/api_report.html --self-contained-html || true
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'api_report.html',
                        reportName: 'API Execution Report'
                    ])
                }
            }
        }
        stage('Performance Testing Stage') {
            agent { label 'Perf-Testing' }
            steps {
                cleanWs()
                checkout scm
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest tests/test_perf.py --html=reports/perf_report.html --self-contained-html || true
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'perf_report.html',
                        reportName: 'Performance Execution Report'
                    ])
                }
            }
        }
        stage('Security Testing Stage') {
            agent { label 'Sec-Testing' }
            steps {
                cleanWs()
                checkout scm
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest tests/test_security.py --html=reports/security_report.html --self-contained-html || true
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'security_report.html',
                        reportName: 'Security Execution Report'
                    ])
                }
            }
        }
        stage('Database Testing Stage') {
            agent { label 'DB-Testing' }
            steps {
                cleanWs()
                checkout scm
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        pytest tests/test_db.py --html=reports/db_report.html --self-contained-html || true
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'db_report.html',
                        reportName: 'Database Execution Report'
                    ])
                }
            }
        }
    }
}
