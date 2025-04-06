import json
import urllib3
import boto3

def lambda_handler(event, context):
    city = "Pune"  # Your city
    api_key = "9fc805f353c8e3bc89be8f5059f0acf9"  # Paste your real API key
    sns_topic_arn = "arn:aws:sns:us-east-1:719629165198:WeatherAlearts"  # Paste your SNS Topic ARN

    http = urllib3.PoolManager()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = http.request('GET', url)
    data = json.loads(response.data.decode('utf-8'))

    print("Full API Response:", data)

    # Handle error if API fails
    if 'weather' not in data:
        print("ERROR: 'weather' key not found. API may have failed.")
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to get weather data')
        }

    weather = data['weather'][0]['main']

    # Force alert for testing
    if True:
        sns = boto3.client('sns')
        message = f"Test Alert: It's going to rain in {city}. Carry an umbrella!"
        sns.publish(TopicArn=sns_topic_arn, Message=message, Subject='Rain Alert')

    rturn {
        'statusCode': 200,
        'body': json.dumps(f"Weather checked successfully: {weather}")
    }
