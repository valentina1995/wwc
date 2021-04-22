run_flask_app:
	@python webapp/run.py

run_rasa_server:
	@rasa run --model ml/chatbot/restaurant/models

run_rasa_actions:
	@rasa run actions --actions ml.chatbot.restaurant.actions
