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

    def generate_itinerary(self, preferences, persona="local"):
        """
        Generates a detailed itinerary based on the user's preferences and selected persona.
        :param preferences: The user's travel preferences (city, start time, end time, budget)
        :param persona: The persona to guide the itinerary (choices: "local", "budget", "luxury")
        :return: Generated itinerary
        """

        # Persona-specific instructions
        if persona == "local":
            persona_instruction = "You are a local travel guide with insider knowledge of the city, recommending authentic and unique experiences that locals enjoy."
        elif persona == "budget":
            persona_instruction = "You are a budget-conscious travel guide, suggesting affordable options for food, transportation, and activities, while still offering an enjoyable experience."
        elif persona == "luxury":
            persona_instruction = "You are a luxury travel expert, focusing on high-end experiences, exclusive landmarks, fine dining, and top-tier services for a lavish journey."
        else:
            persona_instruction = "You are a local travel guide, recommending general experiences."

        # Crafting a more detailed and clear prompt with the selected persona
        prompt = (f"As a travel guide, {persona_instruction} Create a detailed one-day itinerary for a visit to {preferences.city}. "
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


