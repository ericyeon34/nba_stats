import os

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adam_silver:root@localhost:3306/nba_stats'
	SQLALCHEMY_TRACK_MODIFICATIONS = False