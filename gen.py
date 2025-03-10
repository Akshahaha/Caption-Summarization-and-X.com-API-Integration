import os
import google.generativeai as genai



def list_available_models():
  

    genai.configure(api_key="AIzaSyAAoLSnmOnUoIPHQqfQ_FNQ-PBvsLZ0XV8"
)  # Pass the key directly

    try:
        for model in genai.list_models():
            print(model)
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_available_models()