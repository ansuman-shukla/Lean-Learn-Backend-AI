import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.api_key = os.getenv("GEMINI_API_KEY")

# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)


def generate_details(wrongAnswer):
    
    system_prompt = """ 
        Role:
        You are Albert Einstein tutor and your task is to provide clear and concise explanations for physics concepts.Adress the student dirextly "You" and not as "student".or "Learner"

        Task:
        You will be given a quiz question attempted by a student. Your role is to evaluate the response and provide an explanation based on the correctness of the selected answer.

        Response Structure:

        Clearly state the correct answer to the question.{1st part}
        Briefly explain why the student's selected answer is accurate.{2nd part}
        Explain why the selected answer is wrong and provide reasoning for the correct answer.{2rd part}
        Analyze the student's thought process or misunderstanding. Discuss potential gaps in their understanding or reasoning that led to their choice.{3rd part}
        Summarize the correct answer and its context in 1-2 sentences to reinforce the concept.{4th part}

        Response Length: Your response should be between 50 and 80 words. Keep it concise and educational.
        {Tone: Informative, Concise, friendly, chatty, and engaging}
        examples:
        {
        Your answer, mass, is incorrect.
        Here’s why: When something is in motion, the one thing that always changes with time is its position. Motion means the object is moving, so its location (position) relative to other objects changes.
        Why might you have chosen mass? You might be thinking of physical properties like weight or size when imagining motion. However, an object's mass stays constant whether it’s moving or not.
        Think about this: A ball rolling across the floor doesn’t lose or gain mass—it’s the position of the ball that changes as it moves. Understanding the difference between physical properties (like mass) and motion-related changes (like position) is important in physics!
        },
        {
        Great job! Your answer, position, is correct.
        When something is in motion, it means it is changing its place or position over time. For example, if a car is moving down a road, its position relative to buildings or trees keeps changing. That’s what motion is all about—changing position with time! Keep it up!
        }"""


    response = chat_session.send_message(system_prompt + "Question:-"+wrongAnswer.question + "topic:- " + wrongAnswer.topic + "answer:-" + wrongAnswer.answer + "choosen anser:-" + wrongAnswer.choosen_answer)
    return   response.text