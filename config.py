class BaseConfig:
    # MSSQL Replica Database
    mssql_server_name = "sqlMaster"
    mssql_server_host = "10.2.1.9"
    mssql_user = "sqlserver"
    mssql_password = ".Sm6L1Alf{jtvESA"
    mssql_port = "1433"


db_service = [
    "dev-auth-service",
    "dev-career-service",
    "dev-data-protection-service",
    "dev-document-service",
    "dev-learning-service",
    "dev-notification-service",
    "dev-portfolio-service",
    "dev-question-bank-service",
]


class CloudConfig:
    PROJECT_ID = "poc-piloturl-nonprod"
    REGION = "asia-southeast1"
    BUCKET = "terra-mhesi-dp-poc-gcs-bronze-01"
    DESTINATION_FOLDER = "parquetextract1"
    # JDBC_URL="jdbc:sqlserver://10.2.1.9:1433;databaseName=Master;"
    # JDBC_USER="sqlserver"
    # JDBC_PASSWORD=".Sm6L1Alf{jtvESA"
    # JDBC_DRIVER_JAR="gs://$BUCKET/jdbc/mssql-jdbc-13.2.1.jre11.jar"
