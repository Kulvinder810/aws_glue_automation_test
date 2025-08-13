pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Environment Config') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'develop') {
                        env.AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID_DEV')
                        env.AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY_DEV')
                        env.S3_BUCKET             = 'my-bucket-dev'
                        env.GLUE_JOB_NAME         = 'glue-hello-world-dev'
                    } else if (env.BRANCH_NAME == 'test') {
                        env.AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID_TEST')
                        env.AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY_TEST')
                        env.S3_BUCKET             = 'my-bucket-test'
                        env.GLUE_JOB_NAME         = 'glue-hello-world-test'
                    } else if (env.BRANCH_NAME == 'main') {
                        env.AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID_PROD')
                        env.AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY_PROD')
                        env.S3_BUCKET             = 'my-bucket-prod'
                        env.GLUE_JOB_NAME         = 'glue-hello-world-prod'
                    } else {
                        error "Unknown branch: ${env.BRANCH_NAME}"
                    }
                }
            }
        }

        stage('Deploy Script to S3') {
            steps {
                sh """
                aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                aws configure set region $AWS_REGION
                aws s3 cp scripts/hello_world.py s3://$S3_BUCKET/scripts/hello_world.py
                """
            }
        }

        stage('Trigger Glue Job') {
            steps {
                sh "aws glue start-job-run --job-name $GLUE_JOB_NAME"
            }
        }
    }
}