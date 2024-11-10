import transformers
from transformers import pipeline
import torch

class LLM:
    def __init__(self):
        model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
        # Using fp16 precision for better performance and efficiency
        self.model = pipeline("text-generation", 
                              model=model_id, 
                              model_kwargs={"torch_dtype": torch.float16}, 
                              device_map="auto")

    def generate_itinerary(self, preferences):
        # Crafting a more detailed and clear prompt
        prompt = (f"As a travel guide, create a detailed one-day itinerary for a visit to {preferences.city}. "
                  f"The itinerary should start at {preferences.start_time} and end at {preferences.end_time}. "
                  f"Consider a budget of {preferences.budget}. Include suggestions for key landmarks, meal stops, "
                  f"transportation options, and some unique local experiences. Only give response don't repeat back the prompt.")
        
        # Generating the response with settings for enhanced output control
        response = self.model(prompt, 
                              max_length=1000,  # Increase the max length to accommodate longer responses
                              num_return_sequences=1, 
                              temperature=0.7, 
                              top_p=0.9,
                              truncation=True,  # Ensure truncation if the response exceeds max_length
                              pad_token_id=50256)  # Ensuring padding if necessary for models like GPT

        # Extracting the relevant itinerary from the generated text
        generated_text = response[0]['generated_text']
        itinerary = generated_text.split("Only give response don't repeat back the prompt.")[1].strip()
        
        return itinerary



# import transformers
# from transformers import pipeline
# import torch


# class LLM:
#     def __init__(self):
#         model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
#         # Using fp16 precision for better performance and efficiency
#         self.model = pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.float16}, device_map="auto")

#     def generate_itinerary(self, preferences):
#         # Crafting a more detailed and clear prompt
#         prompt = (f"As a travel guide, create a detailed one-day itinerary for a visit to {preferences.city}. "
#                   f"The itinerary should start at {preferences.start_time} and end at {preferences.end_time}. "
#                   f"Consider a budget of {preferences.budget}. Include suggestions for key landmarks, meal stops, "
#                   f"transportation options, and some unique local experiences. Only give response don't repeat back the prompt")
        
#         # Generating the response with settings for enhanced output control
#         response = self.model(prompt, max_length=500, num_return_sequences=1, temperature=0.7, top_p=0.9)
#         return response[0]['generated_text'].split("Only give response don't repeat back the prompt")[1]

# class LLM:
#     def __init__(self):
#         model_id = "meta-llama/Meta-Llama-3-8B"
#         # self.model = pipeline('text-generation', model='llama3')
#         self.model = pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")
    
#     def generate_itinerary(self, preferences):
#         prompt = f"Generate a one-day itinerary for a visit to {preferences.city}. Start at {preferences.start_time} and end at {preferences.end_time}. Budget is {preferences.budget}."
#         response = self.model(prompt)
#         return response[0]['generated_text']
